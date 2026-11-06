# lab8-github

**Git asoslari** fanidan 8-laboratoriya ishi uchun namunaviy repozitoriya.

Bu repozitoriyada GitHub'ning jamoaviy ishlash vositalari amalda sinab ko'riladi:
pull request orqali branchlarni birlashtirish, hamkorlarga (collaborators) kirish
huquqini berish va `main` branchini to'g'ridan-to'g'ri o'zgartirishdan himoyalash.

## Tarkibi

| Fayl | Vazifasi |
|------|----------|
| `app.py` | Oddiy konsol dasturi - omborning asosiy kodi |
| `.gitignore` | Python uchun vaqtinchalik fayllarni e'tiborsiz qoldiradi |

## Ishga tushirish

```bash
git clone https://github.com/nyxeldev/lab8-github.git
cd lab8-github
python app.py
```

## Ishlash tartibi

1. Yangi branch ochiladi: `git switch -c feature/<nom>`
2. O'zgarish commit qilinadi va push qilinadi
3. GitHub'da **Pull request** ochiladi
4. Ko'rib chiqilgandan so'ng `main` ga merge qilinadi

> `main` branchiga to'g'ridan-to'g'ri push qilish taqiqlangan -
> barcha o'zgarishlar faqat pull request orqali kiritiladi.

## Muallif

Jahongir Hamidov (GitHub: [@nyxeldev](https://github.com/nyxeldev))
Axborot xavfsizligini boshqarish, 4-kurs
