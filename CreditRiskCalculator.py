''' Credit Risk Calculator '''



class CreditRiskCalculator:
    def getInputs(self):
        coll_val = float(input('Enter the Collateral Value: '))
        loan_val = float(input('Enter the Loan Value: '))
        pd = float(input('Enter the Probability of Default: '))
        ead = float(input('Enter the Exposure at Default: '))
        
        return {'cv': coll_val, 'lv': loan_val, 'pd': pd, 'ead': ead}
    
    def calculator(self):
        params = self.getInputs()
        coll_val = params['cv']
        loan_val = params['lv']
        pd = params['pd']
        ead = params['ead']
        
        rr = coll_val / loan_val
        lgd = 1 - rr
        el = pd * lgd * ead
        
        return {'rr': rr, 'lgd': lgd, 'el': el}


def main():
    crc = CreditRiskCalculator()
    comps = crc.calculator()
    
    rr = comps['rr']
    lgd = comps['lgd']
    el = comps['el']
    
    print(f'Recovery Rate (RR) = {rr}')
    print(f'Loss Given Default (LGD) = {lgd}')
    print(f'Expected Loss (EL) = {el}')

if __name__ == '__main__':
    main()


