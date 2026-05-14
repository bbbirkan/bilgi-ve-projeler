# Vercel MCP

Vercel'in MCP protokolünü nasıl desteklediğini açıklayan resmi dokümantasyon + Vercel'in kendi MCP server'ı.

**Docs:** https://vercel.com/docs/mcp  
**Vercel'in MCP server'ı:** https://vercel.com/docs/agent-resources/vercel-mcp

## Ne İşe Yarar

İki ayrı konu:

### 1. Vercel'e MCP Server Deploy Etmek
Yazdığın MCP server'ı Vercel'de host etmek için rehber.
- [vercel.com/docs/mcp/deploy-mcp-servers-to-vercel](https://vercel.com/docs/mcp/deploy-mcp-servers-to-vercel)
- Next.js, Nuxt, SvelteKit gibi JS meta-framework'lerle çalışır
- **Vercel MCP Adapter** paketi kullanılır: `@vercel/mcp-adapter`

### 2. Vercel'in Kendi MCP Server'ı
Claude Code veya başka bir MCP istemcisine Vercel'i bağlamak için hazır server.
- [vercel.com/docs/agent-resources/vercel-mcp](https://vercel.com/docs/agent-resources/vercel-mcp)
- Deployment, domain, log gibi Vercel kaynaklarını AI'dan yönetmek için

## Temel Kavramlar

```
MCP Host    = Claude Desktop, Cursor, ChatGPT (AI uygulaması)
MCP Client  = Host'un bir servise açtığı bağlantı
MCP Server  = Dış servis (veritabanı, API, dosya sistemi vb.)
```

**"MCP, USB-C gibidir"** — Her cihaz için farklı kablo yerine tek standart port.

LLM'ler varsayılan olarak gerçek zamanlı/harici veri görmez. MCP bu boşluğu kapatır: finansal veri, kullanıcıya özel içerik, anlık fiyatlar vb.

## İlgili Vercel Araçları

| Araç | Açıklama |
|------|----------|
| [AI SDK](https://ai-sdk.dev) | TypeScript'te MCP client başlatmak için |
| [AI Gateway](https://vercel.com/docs/ai-gateway) | Tüm modellere tek endpoint |
| [Vercel Agent](https://vercel.com/docs/agent) | Stack'ini bilen Vercel AI agent'ı |
| [Next.js MCP Template](https://github.com/vercel-labs/mcp-for-next.js) | Başlangıç şablonu |

## Kullanım Senaryoları

- Next.js uygulamanı MCP server olarak da deploy etmek istiyorsan
- Claude'un Vercel deployment'larına doğal dilde erişmesini istiyorsan
- AI SDK ile MCP client kuruyorsan

**Kaynak:** [vercel.com/docs/mcp](https://vercel.com/docs/mcp)
