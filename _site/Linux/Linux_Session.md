## Session 是什么？
Session 中的每个进程组被称为一个 job，有一个 job 会成为 session 的前台 job(foreground)，其它的 job 则是后台 job(background)。每个 session 连接一个控制终端(control terminal)，控制终端中的输入被发送给前台 job，从前台 job 产生的输出也被发送到控制终端上。同时由控制终端产生的信号，比如 ctrl + z 等都会传递给前台 job。

一般情况下 session 和终端是一对一的关系，当我们打开多个终端窗口时，实际上就创建了多个 session。

Session 的意义在于多个工作(job)在一个终端中运行，其中的一个为前台 job，它直接接收该终端的输入并把结果输出到该终端。其它的 job 则在后台运行。

## Session 的诞生与消亡
当 session 中的所有进程都结束时 session 也就消亡了。实际使用中比如网络断开了，session 肯定是要消亡的。
另外就是正常的消亡，比如让 session 的领头进程退出。一般情况下 session 的领头进程是 shell 进程，如果它处于前台，我们可以使用 exit 命令或者是 ctrl + d 让它退出。
或者我们可以直接通过 kill 命令杀死 session 的领头进程。这里面的原理是：当系统检测到挂断(hangup)条件时，内核中的驱动会将 SIGHUP 信号发送到整个 session。通常情况下，这会杀死 session 中的所有进程。

session 与终端的关系      
如果 session 关联的是伪终端，这个伪终端本身就是随着 session 的建立而创建的，session 结束，那么这个伪终端也会被销毁。
如果 session 关联的是 tty1-6，tty 则不会被销毁。因为该终端设备是在系统初始化的时候创建的，并不是依赖该会话建立的，所以当 session 退出，tty 仍然存在。只是 init 系统在 session 结束后，会重启 getty 来监听这个 tty。






