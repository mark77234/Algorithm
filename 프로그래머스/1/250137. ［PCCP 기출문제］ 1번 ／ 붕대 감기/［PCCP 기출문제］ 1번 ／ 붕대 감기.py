# t초 동안 붕대를 감은
# 1초마다 x만큼 회복
# t초 연속으로 붕대를 감는다 -> y만큼 체력을 추가로 회복
# 현재 체력 <= 최대 체력

# 기술을 쓰는 도중 몬스터에게 공격 당하면 기술 취소
# 공격을 당하는 순간에는 체력 회복 불가 X
# 기술이 취소 당함, 기술이 끝나면 -> 그 즉시 붕대 감기 다시 사용, 연속 성공 시간 0으로 초기화

# 몬스터에게 공격 받으면 현재체력 줄어듦
# 현재 체력이 0 이하가 되면 캐릭터 사망 (체력 회복 불가)

# 붕대감기 기술의 정보, 캐릭터가 가진 최대 체력, 몬스터의 공격 패턴 -> 끝까지 생존?

# 붕대 감기 기술의 시전 시간, 1초당 회복량, 추가 회복량 - bandage
# 최대 체력 - health
# 몬스터 공격 시간, 피해량 - attacks
# 모든 공격이 끝난 직후 남은 체력 return
# 체력 0 이하일 경우 -1 return

def solution(bandage, health, attacks):
    time, recover, plus = bandage[0],bandage[1],bandage[2]
    max_health = health
    
    times = attacks[-1][0] # 몬스터 마지막 공격시간
    
    cnt = 0
    attacked = False # 공격받았는지 체크
    
    for i in range(times): # 전체 시간 동안
        print(i+1,health)
        for j in range(len(attacks)): # 공격하는 시간 찾기
            if attacks[j][0] == i+1: # 공격하는 시간일 경우
                health -= attacks[j][1] # 체력 감소
                attacked = True # 공격 받음
        
        
        if attacked: # 공격 받았으면
            if health <= 0:
                health = -1
                break
            cnt = 0 # 연속 회복 초기화
            attacked = False # attacked 초기화
            continue # 다음으로
        else: # 아닌 경우
            cnt += 1 # 연속 회복 증가
            if cnt == time: # 연속회복시간 도달했을 경우
                health += plus # 추가회복 먼저 회복
                cnt = 0 # 연속회복 초기화
            health += recover # 원래 기본 회복
            if health >= max_health:
                health = max_health
            
    
    return health
                
        
        