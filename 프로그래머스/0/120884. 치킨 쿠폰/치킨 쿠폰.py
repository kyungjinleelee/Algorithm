# 처음 주문한 치킨의 수 만큼 쿠폰을 받는다.
# 받은 쿠폰으로 서비스 치킨을 주문한다.
# 서비스 치킨을 주문할 때마다 다시 쿠폰이 발급된다. -> 다시 쿠폰 모아서 추가로 주문할 수 있다.
# 더 이상 쿠폰으로 치킨 살 수 없을 때 까지 반복한다.

def solution(chicken):
    service_chicken = 0
    coupons = chicken
    
    while coupons >= 10:
        new_service_chicken = coupons // 10
        service_chicken += new_service_chicken
        coupons = coupons % 10 + new_service_chicken
    return service_chicken
        
    