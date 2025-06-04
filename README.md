# destroyed this ahh thing
![your_network_isnt_good](https://raw.githubusercontent.com/hemusuku86/fastly_browser_check_reverse/refs/heads/main/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88%202025-06-05%20003639.png)
# usage
```py
import fastly

fastly.pypi_search("requests") # "<!DOCTYPE html> <html lang=..." or "Failed to solve fastly check"
```
# reversed algorithm (so easy)
1. I checked browser console and I found the log "found answer: ..."<br>
2. I put obfuscated code to https://deobfuscate.io and searched "found answer" in simplified code<br>
3. I found the main code for PoW challenge:
```js
var t = function e(e, t) {
    var n = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
    for (var r = 0; r < n.length; r++) for (var i = 0; i < n.length; i++) {
      var o = e + n[r] + n[i];
      if ((0, eW.default)(o).toString() == t) return n[r] + n[i];
    }
    return "";
  };
  var n = function e(e) {
    var n = e.base, r = e.expires, i = e.hmac, o = e.hash;
    console.log("Challenge: ".concat(n, " => ").concat(o));
    var a = t(n, o);
    return console.log("found answer: ".concat(a)), {ty: "pow", base: n, answer: a, hmac: i, expires: r};
  };
```
And i tried with some hash algorithm and SHA-256 was used by fastly.<br>
