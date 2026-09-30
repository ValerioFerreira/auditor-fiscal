-- Tabela dos dados de cada usuário (leituras, marca-texto, respostas das questões...).
-- Rode uma vez no SQL Editor do Neon, depois de ativar a Data API (ver README, "Login com Google").
--
-- Segurança: o Neon valida o token do Google e entrega o "sub" (identificador do usuário) a
-- auth.user_id(). A política abaixo só deixa cada pessoa ler e gravar as próprias linhas, e a
-- lista de chaves e o tamanho máximo impedem que a tabela seja usada para guardar outra coisa.

create table if not exists public.estudos_dados (
  user_id    text        not null default (auth.user_id()),
  chave      text        not null,
  valor      jsonb       not null,
  atualizado timestamptz not null default now(),
  primary key (user_id, chave),
  constraint estudos_dados_chave check (chave in (
    'lidos', 'geral', 'marcas', 'favoritos', 'questoes', 'qfav', 'qrep', 'qfiltro',
    'ultimo', 'ordemDisciplinas', 'filtroTopicos'
  )),
  constraint estudos_dados_tamanho check (octet_length(valor::text) <= 3000000)
);

alter table public.estudos_dados enable row level security;

drop policy if exists "cada usuario acessa so os proprios dados" on public.estudos_dados;
create policy "cada usuario acessa so os proprios dados" on public.estudos_dados
  for all to authenticated
  using (auth.user_id() = user_id)
  with check (auth.user_id() = user_id);

grant usage on schema public to authenticated;
grant select, insert, update, delete on public.estudos_dados to authenticated;
