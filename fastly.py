import requests
import ua_generator
import hashlib

def solve_pow(base, hash):
    c = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    for i in range(len(c)):
        for ii in range(len(c)):
            if hashlib.sha256((base + c[i] + c[ii]).encode()).hexdigest() == hash:
                return c[i] + c[ii]

def pypi_search(query):
  s = requests.Session()
  s.headers = {
    "user-agent": ua_generator.generate(browser="chrome").text
  }
  r = s.get(f"https://pypi.org/search/?q={query}")
  script = r.text.split("script.src = '")[1].split("'")[0]
  r = s.get(f"https://pypi.org{script}")
  datas = r.text.split('init([{"ty":"pow","data":{"base":"')[1]
  base = datas.split('"')[0]
  hmac = datas.split(',"hmac":"')[1].split('"')[0]
  hash = datas.split(',"hash":"')[1].split('"')[0]
  expires = datas.split(',"expires":"')[1].split('"')[0]
  token = datas.split('}}], "')[1].split('"')[0]
  answer = solve_pow(base, hash)
  r = s.post(f"https://pypi.org/{script.split('/')[1]}/fst-post-back", json={"token":token,"data":[{"ty":"pow","base":base,"answer":answer,"hmac":hmac,"expires":expires}]})
  if '"success"}' in r.text:
      return s.get(f"https://pypi.org/search/?q={query}").text
  else:
      return "Failed to solve fastly check"
