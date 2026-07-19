---
name: turkce-commit-mesajlari
description: Git commit mesajlarını Türkçe olarak oluşturur. Commit yazarken, değişiklikleri gözden geçirirken veya "commit yap" denildiğinde kullan.
allowed-tools: Bash
---

# Türkçe Commit Mesajları

## Talimatlar

1. `git diff --staged` komutuyla değişiklikleri incele
2. Türkçe commit mesajı öner:
   - İlk satır: 50 karakter altında özet (şimdiki zaman)
   - Boş satır
   - Detaylı açıklama (ne ve neden, nasıl değil)
   - Etkilenen bileşenler

## Format Kuralları

### İyi Örnekler:
```
Kullanıcı kimlik doğrulama sistemi eklendi

Auth middleware ve JWT token yönetimi entegre edildi.
Şifreleme için bcrypt kullanıldı.

Etkilenen: auth/, middleware/, config/
```

```
API hata mesajları düzeltildi

500 hataları yerine uygun HTTP kodları döndürülüyor.
Validation hataları artık 422 ile dönüyor.

Etkilenen: api/handlers.go:145
```

### Kötü Örnekler:
```
değişiklikler yapıldı          # Çok belirsiz
KULLANICI EKRANI DÜZELTİLDİ    # Büyük harf kullanma
kodlar düzenlendi.             # Noktalama kullanma
```

## Commit Tipleri

- **Eklendi**: Yeni özellik
- **Güncellendi**: Mevcut özellik iyileştirmesi
- **Düzeltildi**: Bug fix
- **Kaldırıldı**: Kod/özellik silme
- **Refactor**: Kod yeniden yapılandırma
- **Test**: Test ekleme/güncelleme
- **Dokümantasyon**: README, yorum vb.

## Best Practices

1. Şimdiki zaman kullan: "eklendi" değil "eklendi" ✓
2. Kısa ve öz ol
3. Teknik detay yerine iş mantığını anlat
4. Breaking change varsa belirt
5. İlgili issue/PR numaralarını ekle
