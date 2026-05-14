# awesome-mcp-servers (appcypher)

Kategori bazlı, güvenlik odaklı alternatif MCP server listesi. punkpeye'nin listesine göre daha küçük ama daha derli toplu. Her kategoride açıklama ve güvenlik uyarısı var. CC0 lisansı.

## Ne İşe Yarar

MCP server'ları kategorilere göre organize ederek bulmayı kolaylaştıran küratörlü liste. punkpeye listesine göre farkı: daha az ama daha seçilmiş server'lar, güvenlik konusunda daha dikkatli.

## Desteklenen MCP İstemcileri

Claude Desktop, Cursor, Zed, Sourcegraph Cody, Continue, GPT Computer Assistant, LibreChat, Goose, Nerve, MCP Router, VS Code Copilot

## Kategori Listesi

| Kategori | İçerik |
|----------|--------|
| **File Systems** | Yerel dosya erişimi, SFTP, S3, WebDAV |
| **Sandbox & Virtualization** | E2B, Microsandbox, Docker |
| **Version Control** | GitHub, GitLab, Git, Phabricator |
| **Cloud Storage** | Google Drive, Box, Microsoft 365 |
| **Databases** | PostgreSQL, SQLite, MongoDB, MySQL, Snowflake |
| **Communication** | Slack, LINE, Linear, Atlassian, ntfy |
| **Monitoring** | Sentry, Raygun, Metoro, VictoriaMetrics |
| **Search & Web** | Brave, Exa, Playwright, Apify, Tavily |
| **Location Services** | Google Maps, IP2Location, QGIS |
| **Marketing** | Facebook Ads, Google Ads, Fathom Analytics |
| **Note Taking** | Obsidian, Notion, Apple Notes, Todoist |
| **Cloud Platforms** | Cloudflare, Kubernetes, Tinybird |
| **Workflow Automation** | Make, Taskade |
| **Social Media** | Bluesky, YouTube, Spotify, TikTok |
| **Finance** | Stripe, PayPal, Coinmarket, ZBD |
| **Security** | Semgrep, MS Entra ID, Netwrix |
| **AI Services** | OpenAI, HuggingFace, LlamaCloud, Creatify |
| **Aggregators** | MCPJungle, Composio Rube, Pipedream, Zapier |
| **IoT** | Coreflux MQTT |

## Güvenlik Uyarısı (önemli)

Bu listedeki server'ları sandbox'sız çalıştırırken dikkatli ol:
- **Sistem erişimi:** Host process'in izinleriyle çalışır
- **Kod çalıştırma:** İstediği komutu çalıştırabilir
- **Prompt injection riski:** Kötü niyetli içerik tetikleyebilir

**Öneri:** Resmi (⭐) server'ları tercih et, VM'de çalıştır, kodu kur öncesi incele.

## punkpeye ile Farkı

| | punkpeye | appcypher |
|--|---------|-----------|
| Server sayısı | 2,600+ | ~100-150 |
| Güncelleme | Çok sık | Daha seyrek |
| Güvenlik notu | Yok | Kapsamlı uyarı |
| Organizasyon | Tek uzun liste | Temiz kategoriler |
| Odak | Miktar | Kalite seçkisi |

## Araç Yöneticileri (server kurulumunu kolaylaştırır)

- **mcp-get** — CLI, NPM server'larını otomatik kurar
- **mxcp** — SQL/Python ile enterprise MCP tools
- **yamcp** — Workspace bazlı MCP manager
- **ToolHive** — Container'lı güvenli deployment

**Kaynak:** [appcypher/awesome-mcp-servers](https://github.com/appcypher/awesome-mcp-servers) · CC0
