# MCP Orchestration — Model Context Protocol Ajan Mimarisi

## Ne Zaman Kullan
- Yeni MCP server kuracaksan veya değerlendiriyorsan
- HTTP endpoint → LLM ajan köprüsü tasarlarken
- Hangi MCP server'ı seçeceğine karar verirken
- Multi-agent A2A koordinasyonu kurarken

---

## MCP Nedir (Kısa)

Model Context Protocol — LLM'lerin dış araçlara, verilere ve API'lere güvenli erişimi için standart protokol. JSON-RPC 2.0 üzerine kuruludur.

```
LLM ←→ MCP Client ←→ MCP Server ←→ Tool/Data/API
```

MCP server 3 şey sunabilir:
- **Tools** — fonksiyon çağrıları (write, delete, execute)
- **Resources** — okunabilir veri (dosyalar, DB, API yanıtları)
- **Prompts** — yeniden kullanılabilir prompt şablonları

---

## 2026 Top MCP Server Kategorileri

| Kategori | Öne Çıkanlar | Birkan için |
|----------|-------------|-------------|
| **Kod/Dosya** | `codebase-memory-mcp` (CBM), Filesystem MCP | ✅ CBM zaten kurulu |
| **Context Yönetimi** | `context-mode` | ✅ Token tasarrufu için |
| **Veritabanı** | PostgreSQL MCP, SQLite MCP | n8n DB için değerlendirilebilir |
| **Web/Arama** | Tavily MCP → CLI tercih et | CLI daha az context harcar |
| **GitHub** | GitHub MCP | PAT ile zaten çalışıyor |
| **Not/Belge** | Obsidian MCP | Beynim vault için |
| **İzleme** | Grafana MCP | VPS monitoring |
| **Otomasyon** | Appwrite → CLI tercih et | CLI daha verimli |

---

## MCP Gateway'ler (2026)

MCP Gateway — birden fazla MCP server'ı tek endpoint altında toplar:

1. **Cloudflare Workers AI** — edge'de MCP gateway
2. **AWS Bedrock AgentCore** — enterprise MCP hosting  
3. **LangChain MCP adapters** — mevcut LangChain tool'larını MCP'ye çevirir
4. **Composio** — 100+ entegrasyon, MCP uyumlu
5. **Smithery** — MCP marketplace (keşif için)

**Birkan için tavsiye:** Smithery'yi yeni server keşfetmek için tara. Gereksiz server yükleme — context şişirir.

---

## CLI vs MCP — Seçim Kuralı

```
Kural: Bir araç CLI sunuyorsa → MCP yerine CLI kullan

Neden: MCP server tool tanımlarını session başında yükler
       → Her araç = ekstra context = para

Örnek:
  Tavily:   tvly "sorgu"          ← ✅ CLI
  Appwrite: appwrite [komut]      ← ✅ CLI
  vs
  Tavily MCP server               ← ❌ ekstra context

İstisna: Gerçek kaynak/veri erişimi gerekiyorsa MCP mantıklı
         (CBM, context-mode gibi)
```

---

## A2A Protocol (Agent-to-Agent)

Google'ın A2A protokolü: ajanların birbirini keşfetmesi ve görev delege etmesi için standart.

```
AgentA.capabilities → AgentB.task_request → AgentB.response
```

Birkan'ın Orchester sistemindeki Claude ↔ AGY ↔ OpenCode koordinasyonu zaten A2A benzeri. Farkı: A2A'da capability discovery resmi ve otomatik.

**2026 durumu:** MCP daha olgun, A2A daha yeni. İkisi tamamlayıcı: MCP tool erişimi, A2A ajan koordinasyonu için.

---

## HTTP Endpoint → LLM Ajan Köprüsü

VPS'teki FastAPI servisleri (portlar 8000-8006) LLM ajanlarına bağlamak için:

```python
# Basit MCP server şablonu — FastAPI servisini sararlar
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("birkan-services")

@mcp.tool()
def call_nexus_api(endpoint: str, params: dict) -> str:
    """VPS'teki Nexus API'ye çağrı yapar"""
    import httpx
    # Container içinden host'a erişim: 10.0.0.1:<port>
    resp = httpx.get(f"http://10.0.0.1:8001/{endpoint}", params=params)
    return resp.text

if __name__ == "__main__":
    mcp.run()
```

**Not:** Container içinden host servisine `127.0.0.1` değil `10.0.0.1` kullan (Traefik bridge kuralı).

---

## Birkan'ın MCP Kurulum Durumu

| MCP | Durum | Not |
|-----|-------|-----|
| `codebase-memory-mcp` (CBM) | Kurulabilir | `claude-code-harness` skill'ini de oku |
| `context-mode` | Kurulabilir | CBM ile birlikte kullan |
| `n8n-mcp` | `2026 Kalyon.net n8n-mcp/` var | Aktif proje |
| Filesystem MCP | Yerleşik | Claude Code zaten destekler |

---

## MCP Yönetim Komutları

```bash
claude mcp list                    # aktif server'ları listele
claude mcp get <isim>              # detay
claude mcp remove <isim>          # kaldır (gereksiz olanları)
claude mcp add --scope local <..> # repo-spesifik ekle
claude mcp add --scope user <..>  # tüm projelerde kullan
```

**Kural:** `--scope user` sadece gerçekten her projede lazım olanlar için. Çoğunu `--scope local` yap.
