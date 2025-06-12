def hanoi(n,src,dst,temp):
    if n==1:
       print(f"MOVING DISK CALLED 1 ---FROM-->{src}(POLE)--TO-->{dst}(POLE)")
       return
    hanoi(n-1,src,temp,dst)
    print(f"MOVING DISK CALLED{n} --FROM-->{src}(POLE) --TO-->{dst}(POLE)")
    hanoi(n-1,temp,dst,src)
hanoi(3,'A','C','B')