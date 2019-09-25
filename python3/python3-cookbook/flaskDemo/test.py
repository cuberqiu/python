import hashlib

from flask.json.tag import TaggedJSONSerializer
from itsdangerous import URLSafeTimedSerializer
from tornado import web

def get_current_user_idex(secret_cookie, secret_key):
    if not secret_cookie:
        return

    salt = 'cookie-session'
    serializer = TaggedJSONSerializer()
    signer_kwargs = {
        'key_derivation': 'hmac',
        'digest_method': hashlib.sha1
    }
    s = URLSafeTimedSerializer(secret_key, salt=salt, serializer=serializer, signer_kwargs=signer_kwargs)
    try:
        session = s.loads(secret_cookie)
        return session['user']
    except Exception as err:
        raise err

secret_cookie = web.RequestHandler.get_cookie('session', {})
# secret_cookie = """jupyterhub-hub-login="2|1:0|10:1541343951|20:jupyterhub-hub-login|44:YjY5M2EzYmI2NjdlNDc5NWE1MzRhNGQxNTZkNGYwOGQ=|1873683c2f67fbdf554d05d3ac0f152579261d8f8bed029c12e37edd1f84f7e5"; x_host_key=16463aa5472-6c40b21bc0f3b2ca7f2c834610ea1eb3a632305d; pgv_pvid=5693413262; pgv_pvi=361239552; pgv_si=s9529296896; x-host-key-oaback=164a686892f-51442e8c373fdf20fcfe42b68e5f9139560959a9; x-host-key-idcback=164b1b7d0d8-e5a743576b1d3b92840f5e1a76c45ad2cd7fdebf; ASSESS_PPE=shPi9qHreQmQVEvsWsKKSJUW7AbrmCAuVPfbiEv392zdqWvct3gpKBnRInT43kDAC5OldI9ytx7kUSGBvT%2b3kipxWglKvb%2fJ9jXLeaw4y9D8vGRedyID17vflNT4wniCNdJ3tr57k8LlmaUVfMLjMr%2b%2bN32GRJcOySAm3I0pSc5XHFoQx3ZqbmFt%2fVEU%2b1%2bs3yHykaQm1hHWOKkpIAhZEpouNGuiJH4lUBcWHPA3o5KBt1pZ5PtTB3ald5%2bNugQrWiB9YEaW0RhpoNvn6qxSRyeeW2BszDeWwJf%2bvphw%2b66axO7tKLH29b5GdvwHeNVW0SBihh5T4zz%2fwP%2fJgDi4rSpHxsO8cfyiy46QDIuM71u5OimCLjGcKO7qV583DbWx; Tencent.OA.MyWorkspace.MyOAV2=24C775D6D2E943C934C61004DCBB4FA4ED9F95A6DF6F66AE4D9526607D37BD215E441B825C3FE783B3772E64297555CD4C77A9CB56D53C2A1A3E548585A6CA2FB79EB29685D4E2A0D5495E75EAAF2CFD0E9129997ACC151B5C94D046231BD432EF27ABEFBCAAD5984035DDC3AA31FB6DA947C82DB00856CD83E240B575FF1E0E2F9553C5D692BA1919E548ADA0638641; pgv_info==undefined&ssid=s4763816359; jupyterhub-session-id=cd9457c2ceb84e18b3b254ea4158387e; t_u=100707182abb965a%7C45a8d14d63b93aec; t_uid=cuberqiu; OA_TCOA_TICKET=tof:67C342033ED014D02223FD00D429F77DD4355A926694C7801A1C66EB3CD5E04E7B5414F9EDD3E67FA71B5DB4FB82A332D0E71F32D8EC7833F48FEF3750E0AA06C1BCC561BFF5E6484021B398623FEBC02127D74D2FD28C6006BFBBCDC132F9AE65F6C883D5E6EEE9A99C8BF879F40A11FF7FA81C983BF6A2188953B535C990903A3E83CF82493D2CFFFCCFC02E0E0240764AC53EDAF1828988B6A1AC286B13642D74CA5B6A146814D7208D927480F35965A3B54CA91053B9; _xsrf=2|a5f341a9|6f2d977b3b55b26ebc6ea3c9649a7934|1540281801; RIO_TCOA_TICKET=tof:49AA662B7BD8DEAFD8F9A693743DA865140C3C648C862EE5CE80B7FD6E09FDB4FABA91B214121923A5B6E70AC7622A84264D60F780D659C6281DECDE595F4051289B52FBF64A7152B39B29D6DC0FC0450BAB05D205317F17026F990D830C522C07AABAB6AB936746848BD284D3559FCAC30FC6722525D6A96512BD9888C0BBF563E816459AB8F18977A8EBECD9E288A917A12F817816D51F9F3E3B26BB95AF79B63EE764D39E8FB1997AA53B3518223953E648F834F16615; TCOA_TICKET=C472CCD53B14DDE69CE8AB575306EDD45108731A3E4887EB840FDF2D19BB91829398054A199581F6E496068E4782409AD38B5C7953D96F40EB4BCA15221164223320B69C9A38B244BC71346ABDBCBD2CDD0A82F222A0F37CD1F318430F8E9B4F96F3404873ED32A7212DD9159A0153D3EACB53635E1DE2E011141E73B9A3CDB2BC079962BBF2638A3C43B67E5A41816C5373CD80AE672C9D7AD2EDF8BF87E7DD; TCOA=vf0YqRxMzI"""
# secret_cookie = '.eJxdksFuwjAMht8lZ0bTMkrX27RddtieACkyrVsy0qQkDgIh3n1OxwDtYrW_7c_xn5xFDOhFfRZwAAL-Eluisc6yFk5x7mDeuCH7zYWsiRv0ex2z0btOG5x_j72YiWarLQZUFgZkwDq-yE3OscRqHcsGC65psYNoSDUmBkoTBZkHueUBGwipnTDQQ2Z0zojaRmPuWhjB76ZDGw1hGlkVuFzHZb6ST7rFo7pS7uN8dAYsSz1oEHVeyuVMDEheNyGhNjGcuExyxQBHBeOYwFX61VYNODif8nlelM9X8fDmPKaqJIxoW237v8bE8dHafxK73d5hN8UDpdXl_Kbc2FJcGD6ZIHpeq1f3_S7JEvaCBrQ02VAuV5LjokQ2A1cLjotOphvBSjxWM4VNqBYz0cFuegEM67QPpIzrtRV1BybgTOigoCF94PORjyxcb_nvLTB1Hx2xpSVv7EzKvb5_fnxxImAI2llldIekU9uqkPJy-QF6ls_r.DsCiww.XX-AI4u0vCIikrzjkdgR5s1_bzY'
secret_cookie=".eJxdksFuwjAMht8lZ0bTMkrX27RddtieACkyrVsy0qQkDgIh3n1OxwDtYrW_7c_xn5xFDOhFfRZwAAL-Eluisc6yFk5x7mDeuCH7zYWsiRv0ex2z0btOG5x_j72YiWarLQZUFgZkwDq-yE3OscRqHcsGC65psYNoSDUmBkoTBZkHueUBGwipnTDQQ2Z0zojaRmPuWhjB76ZDGw1hGlkVuFzHZb6ST7rFo7pS7uN8dAYsSz1oEHVeyuVMDEheNyGhNjGcuExyxQBHBeOYwFX61VYNODif8nlelM9X8fDmPKaqJIxoW237v8bE8dHafxK73d5hN8UDpdXl_Kbc2FJcGD6ZIHpeq1f3_S7JEvaCBrQ02VAuV5LjokQ2A1cLjotOphvBSjxWM4VNqBYz0cFuegEM67QPpIzrtRV1BybgTOigoCF94PORjyxcb_nvLTB1Hx2xpSVv7EzKvb5_fnxxImAI2llldIekU9uqkPJy-QF6ls_r.DsCiww.XX-AI4u0vCIikrzjkdgR5s1_bzY"
secret_key = "A0s3r98j/3ys R~XHH!3mN4LWX/,?RT"


session = get_current_user_idex(secret_cookie, secret_key=secret_key)
if not session:
    raise web.HTTPError(status_code=403, log_message='Not Authentication')

print(session)
