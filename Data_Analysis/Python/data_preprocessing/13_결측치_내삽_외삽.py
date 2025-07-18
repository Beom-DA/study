####### 결측치 내삽 및 외삽하기

### interpolate 메소드
# 결측치를 주변의 값을 감안하여 보간
# method 인자를 통해 보간하는 방법 설정 가능(spline, polynomial 등)
# limit_direction 인자를 통해 지정된 방향으로 결측치를 보간
# limit 인자를 통해 보간할 결측치의 최대 수 지정

import pandas as pd
import numpy as np

s = pd.Series(
    [1,2,3,np.nan,np.nan,np.nan,7,8,np.nan]
)

s.interpolate(method='spline', order = 1, limit_direction='forward', limit=2)

s = s.interpolate(method='slinear', limit_direction='forward', limit=2)
print(s)