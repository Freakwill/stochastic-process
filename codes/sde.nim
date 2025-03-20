
# Nimble lang for numerical SDE

import std/[math, random, strformat]

# 定义要解决的随机微分方程的漂移项和扩散项
func drift(x: float, mu: float): float =
    mu * x

func diffusion(x: float, sigma: float): float =
    sigma * x

# Euler-Maruyama方法
proc eulerMaruyama(t0: float, T: float, x0: float, dt: float, mu: float,
                  sigma: float): seq[float] =
    var currentX = x0
    var resultSeq = @[currentX]
    let n = int(floor((T - t0) / dt))
    
    for _ in 0..<n:
        # from 0 to n-1, range(n)
        let dw = math.sqrt(dt) * gauss(0.0, 1.0)
        currentX = currentX + drift(currentX, mu) * dt + diffusion(currentX, sigma) * dw
        resultSeq.add(currentX)
    return resultSeq

# 主程序
const default = 1.0
let t0 = 0.01
let T = default
let x0 = 1.0
let dt = 0.01
let mu = 0.05
let sigma = 0.2

# 初始化随机数生成器
randomize()
let solution = eulerMaruyama(t0, T, x0, dt, mu, sigma)

# 输出结果
for i, val in solution.pairs:  # enumerate
    echo fmt"{t0 + i.float * dt}: {val}" # print

import plotly
var times = newSeq[float]()
var values = newSeq[float]()
for i, val in solution.pairs:
    times.add(t0 + i.float * dt)
    values.add(val)

# 使用 plotly 的 newTrace 创建散点图
let trace = plotly.newTrace(
    x=times,
    y=values,
    mode="lines",
    name="Euler-Maruyama Solution"
)

# 创建布局
let layout = plotly.newLayout(
    title="Euler-Maruyama Method for SDE",
    xaxis=plotly.newAxis(title="Time"),
    yaxis=plotly.newAxis(title="X(t)")
)

# 创建并显示图表
let plot = plotly.newPlot(data=[trace], layout=layout)
plot.show()