
### OTOMATİK Öğrenim [2026-06-27]
> Listeleme bileşenlerinde `map()` ile render ederken mutlaka `key` prop'u geçmek gerekiyor (index de olabilir) — yoksa React console warning verir.
>
> Hermes kod review skill'ine 'rendered list must have unique key prop' kuralını ekle; opencode run ile yazılan React kodlarında bu pattern otomatik kontrol edilsin.
