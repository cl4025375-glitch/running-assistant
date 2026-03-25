from fastapi import FastAPI
from fastapi.responses import HTMLResponse, StreamingResponse
import httpx

app = FastAPI()

API = "https://6s4tyg8nhs.coze.site/stream_run"
TOKEN = "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjhkMjgyYTVkLWJlMmUtNDViOS1hODFkLWM4ZGI3MTU5MmExOSJ9.eyJpc3MiOiJodHRwczovL2FwaS5jb3plLmNuIiwiYXVkIjpbInJQMkFqVFJTSnFoMjFGbGQ3VDFFcFdZa2RvNkc3WjR1Il0sImV4cCI6ODIxMDI2Njg3Njc5OSwiaWF0IjoxNzc0NDExMjEyLCJzdWIiOiJzcGlmZmU6Ly9hcGkuY296ZS5jbi93b3JrbG9hZF9pZGVudGl0eS9pZDo3NjIwNzkyMTM3MjEwMTM0NTc0Iiwic3JjIjoiaW5ib3VuZF9hdXRoX2FjY2Vzc190b2tlbl9pZDo3NjIxMDM4MTI3Mjk3MDY5MDk3In0.I6IJwdo_Pjh3l2ApxNtoOp6DOwFwtNgJiIBFYkIypMiCp0m0tIHt3eCGIK0Gpy9x0z6F6UqW-bDvCQCv7dyb3W7kLclXr2UPTn8y1tn_jkwPM9J7sVa4Ft2aJ2sxaAez3XsRxAqoMb-xCLZQxQE9K3wl6E3tL6wNBKZVYfUjeDMWVzKZfxaEM7smHSO3MkBQpJh3nJhpxm3OgWBQideUP27FAloBiF6e6qqNLbs9OcBzx-SoVC_G0vylM6bHTEEw60Bgb--Dtm06KRldejGrOdCxYoRXrmo2EHUc1SgvELvQ5R6SDs-oRgAwkPhSLVvVENr_50qKB3T2k6nCTFtgHw"
PID = "7620789407074861065"

HTML = '''<!DOCTYPE html>
<html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>跑步助手</title>
<style>*{margin:0;padding:0;box-sizing:border-box}body{font-family:-apple-system,sans-serif;background:linear-gradient(135deg,#667eea,#764ba2);min-height:100vh;display:flex;justify-content:center;align-items:center;padding:20px}.c{width:100%;max-width:800px;background:#fff;border-radius:20px;box-shadow:0 20px 60px rgba(0,0,0,.3);overflow:hidden;display:flex;flex-direction:column;height:90vh}.h{background:linear-gradient(135deg,#667eea,#764ba2);color:#fff;padding:20px 30px;display:flex;align-items:center;gap:15px}.q{display:flex;flex-wrap:wrap;gap:8px;padding:15px 20px;background:#f8f9fa}.qb{padding:8px 16px;background:#fff;border:1px solid #ddd;border-radius:20px;cursor:pointer;font-size:13px}.qb:hover{background:linear-gradient(135deg,#667eea,#764ba2);color:#fff;border-color:transparent}.cc{flex:1;overflow-y:auto;padding:20px;background:#f5f5f5}.m{margin-bottom:15px;display:flex;gap:10px}.m.u{flex-direction:row-reverse}.a{width:40px;height:40px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:20px}.m.u .a{background:#667eea;color:#fff}.m.s .a{background:#764ba2;color:#fff}.b{max-width:70%;padding:12px 18px;border-radius:18px;line-height:1.6;white-space:pre-wrap}.m.u .b{background:linear-gradient(135deg,#667eea,#764ba2);color:#fff}.m.s .b{background:#fff;color:#333;box-shadow:0 2px 8px rgba(0,0,0,.1)}.ic{padding:20px;background:#fff;border-top:1px solid #eee;display:flex;gap:10px}.ic textarea{flex:1;padding:12px 18px;border:2px solid #eee;border-radius:25px;outline:0;font-size:15px;resize:none}.sb{width:50px;height:50px;border-radius:50%;background:linear-gradient(135deg,#667eea,#764ba2);border:0;color:#fff;font-size:20px;cursor:pointer}.sb:disabled{opacity:.5}.t{display:flex;gap:4px;padding:12px 18px}.t span{width:8px;height:8px;border-radius:50%;background:#667eea;animation:bo 1.4s infinite}.t span:nth-child(2){animation-delay:-.16s}@keyframes bo{0%,80%,100%{transform:scale(0)}40%{transform:scale(1)}}@media(max-width:600px){.c{height:100vh;border-radius:0}.b{max-width:85%}}</style></head>
<body><div class="c"><div class="h"><div style="font-size:40px">🏃</div><div><h1 style="font-size:24px">跑步助手</h1><p style="font-size:14px;opacity:.9">智能记录·数据分析·科学建议</p></div></div>
<div class="q"><button class="qb" onclick="sq('今天跑了5公里，30分钟')">📝记录跑步</button><button class="qb" onclick="sq('最近跑步记录')">📊查看记录</button><button class="qb" onclick="sq('今年跑了多少公里')">📈统计</button><button class="qb" onclick="sq('今天适合跑步吗')">🌤️天气</button></div>
<div class="cc" id="cc"><div class="m s"><div class="a">🤖</div><div class="b">你好！我是跑步助手 🏃

我可以帮你：记录跑步数据、查看历史统计、天气建议、生成图表

点击上方按钮或直接输入！</div></div></div>
<div class="ic"><textarea id="mi" placeholder="输入消息..." rows="1" onkeydown="if(event.key==='Enter'&&!event.shiftKey){event.preventDefault();s()}"></textarea><button class="sb" id="btn" onclick="s()">➤</button></div></div>
<script>let sid='s_'+Date.now();function sq(t){document.getElementById('mi').value=t;s()}async function s(){const i=document.getElementById('mi'),m=i.value.trim();if(!m)return;const b=document.getElementById('btn');b.disabled=true;am(m,'u');i.value='';const l=document.createElement('div');l.className='m s';l.id='ld';l.innerHTML='<div class="a">🤖</div><div class="b t"><span></span><span></span><span></span></div>';document.getElementById('cc').appendChild(l);sc();try{const r=await fetch('/api',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({m,s:sid})});document.getElementById('ld')?.remove();if(!r.ok)throw new Error(r.status);const rd=r.body.getReader(),dc=new TextDecoder();let an='',bf='';while(true){const{done,value}=await rd.read();if(done)break;bf+=dc.decode(value,{stream:true});const ls=bf.split('\\n');bf=ls.pop()||'';for(const l of ls){if(l.startsWith('data:')){try{const d=JSON.parse(l.slice(5).trim());if(d.type==='answer'&&d.content?.answer){an+=d.content.answer;ul(an)}}catch(e){}}}}if(!an)am('暂无回复','s')}catch(e){document.getElementById('ld')?.remove();am('错误:'+e.message,'s')}b.disabled=false;i.focus()}function am(t,tp){const d=document.createElement('div');d.className='m '+tp;d.innerHTML='<div class="a">'+(tp==='u'?'👤':'🤖')+'</div><div class="b">'+e(t)+'</div>';document.getElementById('cc').appendChild(d);sc()}function ul(t){const ms=document.querySelectorAll('.m.s .b');if(ms.length){ms[ms.length-1].textContent=t;sc()}}function sc(){document.getElementById('cc').scrollTop=999999}function e(t){const d=document.createElement('div');d.textContent=t;return d.innerHTML}</script></body></html>'''

@app.get("/")
async def home():
    return HTMLResponse(HTML)

@app.post("/api")
async def api(req: dict):
    payload = {"content":{"query":{"prompt":[{"type":"text","content":{"text":req.get("m","")}}]}},"type":"query","session_id":req.get("s","s1"),"project_id":PID}
    async def stream():
        async with httpx.AsyncClient(timeout=60) as client:
            async with client.stream("POST",API,headers={"Authorization":TOKEN,"Content-Type":"application/json"},json=payload) as r:
                async for c in r.aiter_bytes():yield c
    return StreamingResponse(stream(),media_type="text/event-stream")

if __name__=="__main__":
    import uvicorn
    uvicorn.run(app,host="0.0.0.0",port=8000)
