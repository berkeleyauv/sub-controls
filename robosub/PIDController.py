class PID:

    def __init__(self, p, i , d, thresh=1.0, setpoint=0.0):
        self.p = p
        self.i = i
        self.d = d
        self.setpoint = setpoint
        self.prevIntegral = 0.0
        self.prevError = 0.0
        self.prevTime = 0.0
        self.PID_THRESH = thresh
        self.bias = 0.0

    def reset(self):
        self.prevError = 0.0
        self.prevIntegral = 0.0
        self.prevTime = 0.0

    def setSetpoint(self, setpoint):
        self.setpoint = setpoint

    def pidLoop(self, curVal, curTime):
        error = self.setpoint - curVal
        p_term = self.p*error
        d_term = self.d*(error - prevError)/(curTime - prevTime)
        integral = self.prevIntegral + error*(curTime-prevTime)
        self.prevError = error
        self.prevTime = curTime
        self.prevIntegral = integral
        return P_term + self.i*integral + d_term

    def onTarget(self, curVal):
        return abs(self.setpoint - curVal) < self.PID_THRESH