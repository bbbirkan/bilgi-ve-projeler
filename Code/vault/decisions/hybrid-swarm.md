# Hybrid Swarm Architecture (Ruflo + RecursiveMAS)

**Karar:** Ajan tabanlı sistemlerimizde Ruflo ve RecursiveMAS'ın güçlü yönlerini birleştiren hibrit bir mimari kullanacağız.
**Tarih:** 2026-05-13

## Mimari Vizyon
- **Orkestrasyon Şefi (Brain): Ruflo**
  - Hangi ajanların çalışacağını (ör. Güvenlik Uzmanı, Frontend Geliştirici) belirler.
  - Swarm hiyerarşisini (mesh, ring, vs.) yönetir.
  - SONA ile kendini eğitir ve plugin marketplace yeteneklerini sağlar.
  
- **Sinir Sistemi (Communication Protocol): RecursiveMAS**
  - Ajanların birbirleriyle nasıl konuşacağını belirler.
  - Maliyetli "decode-encode" (metin tabanlı iletişim) döngüsünü kaldırır.
  - Ajanlar "Latent-space" (gizli vektör alanı) üzerinden haberleşir.
  
## Anahtar Talimat
Sistemdeki diğer yapay zekalara ve Hermes'e verilecek anahtar komut şudur:
> *"Ruflo ile bir swarm başlat ama ajanlar arası iletişimi RecursiveMAS latent-space protokolü üzerinden yap."*

## Kazanımlar
1. **Maliyet:** Token kullanımında %75.6 düşüş.
2. **Hız:** İşlemlerde 2.4 kat hızlanma.
3. **Karmaşıklık Yönetimi:** Yüzlerce ajan çakışmadan yönetilebilir.

## Worker (İşçi) Havuzu Entegrasyonu
Ruflo'nun altında çalışacak alt ajanların (worker agents) baştan yazılması yerine, `msitarzewski/agency-agents` reposundaki hazır 80 uzman ajan (bkz. [[entities/agency-agents]]) Hybrid Swarm mimarisine entegre edilebilir.
