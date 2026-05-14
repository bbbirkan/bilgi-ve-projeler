# modelcontextprotocol/servers — Resmi MCP Server Koleksiyonu

Anthropic'in MCP steering group'u tarafından yönetilen **resmi referans implementasyonlar** koleksiyonu. Bunlar production tool değil, kendi server'ını yazarken öğrenmek için örnek kod.

> Gerçek MCP server listesi için: [registry.modelcontextprotocol.io](https://registry.modelcontextprotocol.io/)

## Aktif Referans Server'lar (7 adet)

| Server | Ne yapar |
|--------|----------|
| **Everything** | Test/referans — prompt, resource, tool örnekleri |
| **Fetch** | Web içeriği çeker ve LLM için dönüştürür |
| **Filesystem** | Yapılandırılabilir erişim kontrolüyle yerel dosya işlemleri |
| **Git** | Git repo okuma, arama, manipülasyon |
| **Memory** | Knowledge graph tabanlı kalıcı hafıza sistemi |
| **Sequential Thinking** | Adım adım düşünce zinciriyle problem çözme |
| **Time** | Zaman ve timezone dönüşümleri |

## Arşivlenen Server'lar (artık bağımsız repo'larda)

AWS KB Retrieval, Brave Search (→ official), EverArt, GitHub, GitLab, Google Drive, Google Maps, PostgreSQL, Puppeteer, Redis, Sentry, Slack (→ Zencoder), SQLite

## SDK Desteği

C#, Go, Java, Kotlin, PHP, Python, Ruby, Rust, Swift, TypeScript

## Hızlı Kullanım

```bash
# TypeScript server'ı npx ile çalıştır
npx -y @modelcontextprotocol/server-memory

# Python server'ı uvx ile çalıştır
uvx mcp-server-git
```

**Claude Desktop config:**
```json
{
  "mcpServers": {
    "memory": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-memory"]
    },
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/dir"]
    }
  }
}
```

## Ne Zaman Kullanılır

- MCP server **yazmayı öğreniyorsan** → bu repoyu incele
- Hazır bir server **bulmak istiyorsan** → registry veya punkpeye listesine git
- **Memory server** gibi basit bir tool hızlıca denemek istiyorsan → `npx` ile direkt çalıştır

**Kaynak:** [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) · Apache 2.0 / MIT
