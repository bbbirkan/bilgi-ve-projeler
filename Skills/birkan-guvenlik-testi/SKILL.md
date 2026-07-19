---
name: guvenlik-testi
description: Kod güvenlik açıklarını tespit eder ve düzeltir. OWASP Top 10, injection saldırıları, XSS, authentication zafiyetleri kontrol edilir. Güvenlik testi, penetrasyon testi veya kod analizi istendiğinde kullan.
allowed-tools: Read, Grep, Glob, Bash
---

# Güvenlik Testi ve Analiz

Defensive security, CTF challenges ve educational context için güvenlik analizi yap.

## OWASP Top 10 Kontrol Listesi

### 1. Injection Saldırıları
- **SQL Injection**: Parametrize sorgular kullanılıyor mu?
- **NoSQL Injection**: Input validation var mı?
- **Command Injection**: Shell komutlarında input sanitization?
- **LDAP/XML Injection**: Güvenli parse edilmiş mi?

**Kontrol:**
```bash
# SQL injection riski
grep -rn "execute.*\+" --include="*.py" --include="*.js"
grep -rn "query.*format" --include="*.py"

# Command injection riski
grep -rn "os.system\|subprocess.call" --include="*.py"
grep -rn "exec\|eval" --include="*.js" --include="*.py"
```

### 2. Broken Authentication
- Session timeout var mı?
- Şifre politikası yeterli mi?
- JWT token expiry kontrolü?
- Rate limiting implementasyonu?

**Kontrol:**
```bash
# Zayıf şifre kontrolü
grep -rn "password.*length.*[0-6]" --include="*.py" --include="*.js"

# Session yönetimi
grep -rn "session.*expire\|timeout" --include="*.py" --include="*.js"
```

### 3. Sensitive Data Exposure
- HTTPS kullanılıyor mu?
- Hassas data loglanıyor mu?
- Şifreler hash'leniyor mu (bcrypt, argon2)?
- API keyleri hard-coded değil mi?

**Kontrol:**
```bash
# Hard-coded credentials
grep -rn "password.*=.*[\"\'].*[\"\']" --include="*.py" --include="*.js" --include="*.go"
grep -rn "api_key.*=.*[\"\']" --include="*.env" --include="*.json"

# Plain text passwords
grep -rn "password.*=.*request\." --include="*.py"
```

### 4. XML External Entities (XXE)
- XML parser güvenli konfigüre edilmiş mi?
- External entity processing disabled mı?

### 5. Broken Access Control
- Authorization kontrolleri var mı?
- IDOR (Insecure Direct Object Reference) zafiyeti?
- Privilege escalation riski?

**Kontrol:**
```bash
# Authorization eksikliği
grep -rn "def.*delete\|def.*update" --include="*.py" | head -20
# Her endpoint'te @require_auth gibi decorator var mı?
```

### 6. Security Misconfiguration
- Default credentials kullanılıyor mu?
- Debug mode production'da kapalı mı?
- Error messages detaylı bilgi veriyor mu?
- Security headers eksik mi?

**Kontrol:**
```bash
# Debug mode
grep -rn "DEBUG.*=.*True\|debug.*true" --include="*.py" --include="*.js" --include="*.env"

# Default credentials
grep -rn "admin.*admin\|root.*root" --include="*.py" --include="*.js"
```

### 7. Cross-Site Scripting (XSS)
- Input sanitization yapılıyor mu?
- Output encoding var mı?
- Content Security Policy (CSP) header?

**Kontrol:**
```bash
# Unsafe HTML rendering
grep -rn "innerHTML\|dangerouslySetInnerHTML" --include="*.js" --include="*.jsx" --include="*.tsx"
grep -rn "render_template_string" --include="*.py"
```

### 8. Insecure Deserialization
- pickle/eval kullanılıyor mu?
- User input deserialize edilirken validation var mı?

**Kontrol:**
```bash
# Insecure deserialization
grep -rn "pickle.loads\|yaml.load[^_]" --include="*.py"
grep -rn "JSON.parse.*request" --include="*.js"
```

### 9. Using Components with Known Vulnerabilities
- Dependency güncel mi?
- Security advisories kontrol ediliyor mu?

**Kontrol:**
```bash
# Outdated dependencies
npm audit
pip-audit
go list -m all | nancy sleuth
```

### 10. Insufficient Logging & Monitoring
- Security events loglanıyor mu?
- Failed login attempts tracked?
- Anomaly detection var mı?

**Kontrol:**
```bash
# Logging eksikliği
grep -rn "login\|authenticate" --include="*.py" | grep -v "log\|logger"
```

## Ek Güvenlik Kontrolleri

### CORS Misconfiguration
```bash
grep -rn "Access-Control-Allow-Origin.*\*" --include="*.py" --include="*.js"
```

### Rate Limiting Eksikliği
```bash
grep -rn "@rate_limit\|@throttle\|rateLimit" --include="*.py" --include="*.js"
```

### Cryptographic Failures
```bash
# Weak hashing
grep -rn "md5\|sha1" --include="*.py" --include="*.js" --include="*.go"

# Weak random
grep -rn "random.random\|Math.random" --include="*.py" --include="*.js"
```

## Test Senaryoları

### 1. Input Validation Test
- Special characters: `'; DROP TABLE--`, `<script>alert(1)</script>`
- Path traversal: `../../../etc/passwd`
- Null bytes: `%00`

### 2. Authentication Test
- Brute force protection
- Session fixation
- Password reset token strength

### 3. Authorization Test
- Horizontal privilege escalation (user A → user B)
- Vertical privilege escalation (user → admin)

## Güvenlik Raporlama Formatı

```markdown
## Güvenlik Zafiyet Raporu

### Zafiyet: [İsim]
- **Severity**: Critical/High/Medium/Low
- **CVSS Score**: X.X
- **Konum**: dosya.py:satır
- **Açıklama**: Ne bulundu
- **Impact**: Ne olabilir
- **Proof of Concept**: Nasıl exploit edilir
- **Çözüm**: Nasıl düzeltilir
- **Referans**: OWASP/CWE linki
```

## Best Practices

1. **Defense in Depth**: Katmanlı güvenlik
2. **Least Privilege**: Minimum yetki prensibi
3. **Fail Securely**: Hata durumunda güvenli mod
4. **Input Validation**: Whitelist approach
5. **Output Encoding**: Context-aware encoding
6. **Security Headers**: CSP, HSTS, X-Frame-Options
7. **Regular Updates**: Dependencies güncel tut
8. **Security Testing**: Automated + Manual
9. **Code Review**: Peer review zorunlu
10. **Incident Response**: Hazırlıklı ol

## Araçlar

- **Static Analysis**: Bandit (Python), ESLint, Semgrep
- **Dependency Scan**: npm audit, pip-audit, Snyk
- **SAST**: SonarQube, CodeQL
- **DAST**: OWASP ZAP, Burp Suite
- **Secrets Scan**: TruffleHog, git-secrets
