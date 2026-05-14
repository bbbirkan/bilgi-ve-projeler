---
tags: [entity, ai-tool, agents, swarm]
aliases: [Agency Agents, msitarzewski/agency-agents]
---
# Agency Agents

GitHub reposu `msitarzewski/agency-agents` olan, 10 farklı departmana ayrılmış 80 uzman AI ajanı içeren sistem.

## Özellikler
- Frontend, Backend, DevOps, Tasarım, Pazarlama gibi departmanlar.
- Her ajanın kendi kişiliği, iş akışı ve somut çıktıları vardır.
- Claude Code, Cursor, Windsurf, Aider, Gemini CLI desteği.

## Sistemimizdeki Yeri
- [[decisions/hybrid-swarm]] mimarisinde Ruflo'nun (orkestratör) yönetebileceği hazır "worker" (işçi) ajan havuzu olarak kullanılabilir. Ajan kişiliklerini sıfırdan promptlamak yerine bu repodaki profiller sisteme dahil edilebilir.
