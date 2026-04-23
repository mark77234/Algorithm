def time_to_sec(t):
    minute,second = map(int,t.split(":"))
    
    return minute*60 + second

def solution(video_len, pos, op_start, op_end, commands):
    video_len = time_to_sec(video_len)
    pos = time_to_sec(pos)
    op_start = time_to_sec(op_start)
    op_end = time_to_sec(op_end)
    
    if op_start <= pos <= op_end:
        pos = op_end
    
    for command in commands:
        if command == "next":
            pos += 10
            if pos >= video_len:
                pos = video_len
            if op_start <= pos <= op_end:
                pos = op_end
            
        if command == "prev":
            pos -= 10
            if pos < 0:
                pos = 0
            if op_start <= pos <= op_end:
                pos = op_end
    
    return f"{pos//60:02d}:{pos%60:02d}"