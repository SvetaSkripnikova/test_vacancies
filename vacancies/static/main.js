const DateBox = document.getElementById('date-box')
const deadline = DateBox.getAttribute("cl")

const DateStart = document.getElementById('date-start')
const start = DateStart.getAttribute("cl").toString()

const countdownBox = document.getElementById('countdown-box')

const noww = Number(start)*1000

const endd = noww + parseInt(deadline)*1000*60*60
console.log(noww)
console.log(endd)

const url = window.location.protocol + '//' + window.location.host + '/' + 'applications/'

setInterval(()=>{
    const now = new Date().getTime()
    const diff = endd - now

    const d = Math.floor((endd/(1000*60*60*24))-(now/(1000*60*60*24)))
    const h = Math.floor((endd/(1000*60*60)-(now/(1000*60*60)))%24)
    const m = Math.floor((endd/(1000*60)-(now/(1000*60)))%60)
    const s = Math.floor((endd/(1000)-(now/(1000)))%60)

    if (diff>0){
    countdownBox.innerHTML = "До завершения дедлайна: "+d+":"+h+":"+m+":"+s
    }else {
        window.location.href = url
    }

}, 1000)
