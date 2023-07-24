# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from uuid import uuid4

def fatura_ver(
    tarih:str         = "07/10/1995",
    saat:str          = "14:28:37",
    vkn_veya_tckn:str = "11111111111",
    ad:str            = "Ömer Faruk",
    soyad:str         = "Sancak",
    unvan:str         = "",
    vergi_dairesi:str = "",
    urun_adi:str      = "Python Yazılım Hizmeti",
    fiyat:int | float = 100,
    fatura_notu:str   = "— QNB Finansbank —\nTR70 0011 1000 0000 0118 5102 59\nÖmer Faruk Sancak"
):
    # matrah = fiyat / 1.18     # ! %18
    matrah = fiyat / 1.20       # ! %20
    kdv    = fiyat - matrah
    return {
        "faturaUuid"        : f"{uuid4()}",
        "belgeNumarasi"     : "",
        "faturaTarihi"      : tarih,
        "saat"              : saat,
        "paraBirimi"        : "TRY",
        "dovzTLkur"         : "0",
        "faturaTipi"        : "SATIS",
        "hangiTip"          : "5000/30000",
        "vknTckn"           : vkn_veya_tckn,
        "aliciUnvan"        : unvan,
        "aliciAdi"          : ad,
        "aliciSoyadi"       : soyad,
        "binaAdi"           : "",
        "binaNo"            : "",
        "kapiNo"            : "",
        "kasabaKoy"         : "",
        "vergiDairesi"      : vergi_dairesi,
        "ulke"              : "Türkiye",
        "bulvarcaddesokak"  : "",
        "irsaliyeNumarasi"  : "",
        "irsaliyeTarihi"    : "",
        "mahalleSemtIlce"   : "",
        "sehir"             : " ",
        "postaKodu"         : "",
        "tel"               : "",
        "fax"               : "",
        "eposta"            : "",
        "websitesi"         : "",
        "iadeTable"         : [],
        "vergiCesidi"       : " ",
        "malHizmetTable"    : [
            {
                "malHizmet"                     : urun_adi,
                "miktar"                        : 1,
                "birim"                         : "C62",
                "birimFiyat"                    : f"{round(matrah, 2)}",
                "fiyat"                         : f"{round(matrah, 2)}",
                "iskontoOrani"                  : 0,
                "iskontoTutari"                 : "0",
                "iskontoNedeni"                 : "",
                "malHizmetTutari"               : f"{round(matrah, 2)}",
                "kdvOrani"                      : "20",
                "vergiOrani"                    : 0,
                "kdvTutari"                     : f"{round(kdv, 2)}",
                "vergininKdvTutari"             : "0",
                "ozelMatrahTutari"              : "0",
                "hesaplananotvtevkifatakatkisi" : "0",
            }
        ],
        "tip"                      : "İskonto",
        "matrah"                   : f"{round(matrah, 2)}",
        "malhizmetToplamTutari"    : f"{round(matrah, 2)}",
        "toplamIskonto"            : "0",
        "hesaplanankdv"            : f"{round(kdv, 2)}",
        "vergilerToplami"          : f"{round(kdv, 2)}",
        "vergilerDahilToplamTutar" : f"{round(matrah + kdv, 2)}",
        "odenecekTutar"            : f"{round(matrah + kdv, 2)}",
        "not"                      : fatura_notu,
        "siparisNumarasi"          : "",
        "siparisTarihi"            : "",
        "fisNo"                    : "",
        "fisTarihi"                : "",
        "fisSaati"                 : " ",
        "fisTipi"                  : " ",
        "zRaporNo"                 : "",
        "okcSeriNo"                : "",
    }