''' Liquidity Test '''



class LiquidityTest:
    def getInputs(self):
        # For Liquidity Test-
        curr_assets = float(input('Enter the Current Assets: '))
        curr_liabs = float(input('Enter the Current Liabilities: '))
        
        cash = float(input('Enter the Cash Amount: '))
        acc_recv = float(input('Enter the Account Receivables: '))
        mark_sec = float(input('Enter the Market Securities: '))
        
        
        # For Debt to Equity Ratio-
        total_liabs = float(input('Enter the Total Liabilities: '))
        shareholder_eqty = float(input("Enter the Shareholder's Equity: "))
        
        # For DSCR(Debt Service Coverage Ratio)-
        net_opt_inc = float(input('Enter the Net Operating Income: '))
        debt_serv = float(input('Enter the Debt Service: '))
        
        return {'ca': curr_assets, 'cl': curr_liabs, 'cash': cash, 'ar': acc_recv, 'msec': mark_sec, 'tl': total_liabs, 'seq': shareholder_eqty, 'noi': net_opt_inc, 'ds': debt_serv}
    
    def tester(self, curr_assets, curr_liabs, cash, acc_recv, mark_sec, total_liabs, shareholder_eqty, net_opt_inc, debt_serv):
        # params = self.getInputs()
        
        # For Liquidity Test-
        # curr_assets = params['ca']
        # curr_liabs = params['cl']
        
        
        # cash = params['cash']
        # acc_recv = params['ar']
        # mark_sec = params['msec']
        
        
        # For Liquidity Test-
        curr_ratio = curr_assets / curr_liabs
        quick_ratio = (cash + acc_recv + mark_sec) / curr_liabs
        cash_ratio = (cash + mark_sec / curr_liabs)
        
        
        # For Debt to Equity Ratio-
        debt2eqty = total_liabs / shareholder_eqty
        
        # For DSCR(Debt Service Coverage Ratio)-
        dscr = net_opt_inc / debt_serv
        
        
        return {'curr': curr_ratio, 'qr': quick_ratio, 'cashr': cash_ratio, 'der': debt2eqty, 'dscr': dscr}
    
    def driver(self):
        params = self.getInputs()
        
        
        # For Liquidity Test-
        curr_assets = params['ca']
        curr_liabs = params['cl']
        
        cash = params['cash']
        acc_recv = params['ar']
        mark_sec = params['msec']
        
        
        # For Debt to Equity Ratio-
        total_liabs = params['tl']
        shareholder_eqty = params['seq']
        
        
        # For DSCR(Debt Service Coverage Ratio)-
        net_opt_income = params['noi']
        debt_serv = params['ds']
        
        return self.tester(curr_assets, curr_liabs, cash, acc_recv, mark_sec, total_liabs, shareholder_eqty, net_opt_income, debt_serv)
    
    def checkHealth(self, ratio_name, ratio):
        name = ratio_name.lower()
        
        if name == 'current ratio':
            return True if 1.5 < ratio < 3 else False
        
        elif name == 'quick ratio':
            return True if ratio >= 1 else False
        
        elif name == 'cash ratio':
            return True if ratio > 1 else False
        
        elif name == 'debt to equity ratio':
            return True if 1 <= ratio <= 1.5 else False
        
        elif name == 'debt service coverage ratio':
            return True if 1.25 < ratio < 1.5 else False
        
        else:
            return None
    
    def display(self):
        comps = self.driver()
        
        
        curr_ratio = comps['curr']
        quick_ratio = comps['qr']
        cash_ratio = comps['cashr']
        
        der = comps['der']
        dscr = comps['dscr']
        
        curr_health = self.checkHealth('Current Ratio', curr_ratio)
        quick_health = self.checkHealth('Quick Ratio', quick_ratio)
        cash_health = self.checkHealth('Cash Ratio', cash_ratio)
        
        der_health = self.checkHealth('Debt to Equity Ratio', der)
        dscr_health = self.checkHealth('Debt Service Coverage Ratio', dscr)
        
        
        if curr_health:
            print(f'Current Ratio (Healthy) = {curr_ratio}')
        else:
            print(f'Current Ratio (Unhealthy) = {curr_ratio}')
        
        if quick_health:
            print(f'Quick Ratio (Good) = {quick_ratio}')
        else:
            print(f'Quick Ratio (Risky) = {quick_ratio}')
        
        if cash_health:
            print(f'Cash Ratio (Good) = {cash_ratio}')
        else:
            print(f'Cash Ratio (Risky) = {cash_ratio}')
        
        
        # For Debt to Equity Ratio-
        if der_health:
            print(f'Debt to Equity Ratio (Good) = {der}')
        else:
            print(f'Debt to Equity Ratio (Risky) = {der}')
        
        # For DSCR(Debt Service Coverage Ratio)-
        if dscr_health:
            print(f'Debt Service Coverage Ratio (Healthy) = {dscr}')
        else:
            print(f'Debt Service Coverage Ratio (Unhealthy) = {dscr}')



def main():
    lt = LiquidityTest()
    
    # comps = lt.tester()
    
    # curr_ratio = comps['curr']
    # quick_ratio = comps['qr']
    # cash_ratio = comps['cashr']
    
    
    # print(f'Current Ratio = {curr_ratio}')
    # print(f'Quick Ratio = {quick_ratio}')    
    # print(f'Cash Ratio = {cash_ratio}')
    
    lt.display()

if __name__ == '__main__':
    main()    


