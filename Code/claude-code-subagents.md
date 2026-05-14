# claude-code-subagents (0xfurai)

100+ özelleşmiş Claude Code subagent koleksiyonu. Uniform prompt formatı, MIT lisansı, çoklu dil desteği. `~/.claude/agents/` klasörüne klon yap → hepsi hazır.

## Hızlı Kurulum

```bash
cd ~/.claude
git clone https://github.com/0xfurai/claude-code-subagents.git agents/
```

Sonra Claude Code, bağlama göre otomatik doğru agent'ı seçer. Veya açıkça:
```
"Use the python-expert to optimize this algorithm"
"Get the react-expert to refactor this component"
```

## Kategori Listesi

| Kategori | Örnek agent'lar |
|----------|----------------|
| **Programlama Dilleri** (23) | bash, python, javascript, typescript, java, go, rust, c, cpp, php, ruby, scala, kotlin, swift, dart, lua, haskell, ocaml, perl, csharp, clojure, elixir, erlang |
| **Web / Frontend** (27) | react, vue, angular, svelte, solidjs, nextjs, remix, nestjs, express, fastapi, flask, rails, laravel, gin, fiber, aspnet-core, actix, phoenix, html, css, tailwind, django, fastify |
| **Mobile / Desktop** (8) | react-native, flutter, ios, swiftui, android, electron, tauri, expo |
| **Veritabanları** (15) | sql, postgres, mysql, sqlite, mariadb, mssql, mongodb, redis, neo4j, cassandra, cockroachdb, dynamodb, elasticsearch, opensearch, vector-db |
| **ORM'ler** (5) | prisma, sequelize, typeorm, knex, mongoose |
| **DevOps / Altyapı** (9) | docker, kubernetes, terraform, pulumi, jenkins, github-actions, gitlab-ci, circleci, ansible |
| **Mesajlaşma** (9) | rabbitmq, kafka, nats, mqtt, websocket, grpc, graphql, rest, openapi, trpc |
| **Test** (10) | jest, vitest, mocha, jasmine, ava, cypress, playwright, selenium, testcafe, puppeteer |
| **Data Science / ML** (6) | pandas, numpy, scikit-learn, tensorflow, pytorch, langchain |
| **Monitoring** (5) | prometheus, grafana, loki, elk, opentelemetry |
| **Güvenlik** (3) | owasp-top10, jwt, oauth-oidc |
| **Build Tools** (2) | webpack, rollup |
| **Background Jobs** (3) | celery, sidekiq, bullmq |
| **Runtime** (3) | nodejs, bun, deno |
| **Servisler** (7) | stripe, braintree, sns, sqs, openai-api, auth0, keycloak |

## VoltAgent & wshobson ile Farkı

| | 0xfurai | VoltAgent | wshobson |
|--|---------|-----------|---------|
| Miktar | 100+ | 131+ | 184 |
| Plugin sistemi | Yok | Var | Var |
| Odak | Kapsamlı dil/teknoloji coverage | Kategori bazlı | Enterprise workflow |
| Kurulum | Direkt clone | Plugin / shell | Plugin |

**Kaynak:** [0xfurai/claude-code-subagents](https://github.com/0xfurai/claude-code-subagents) · MIT
