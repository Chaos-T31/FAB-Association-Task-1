''' Piotroski Score '''



class PiotroskiScore:
    def getInputs(self):
        params = ('Net Income', 'Return on Assets (ROA)', 'Operating Cash Flow (CFO)', 'Long Term Debt of the Current Year', 'long Term Debt of the Previous Year', 'Current Ratio of the Current Year', 'Current Ratio of the Previous Year', 'Number of Shares Issued in the Last Year (Shares Dilution)', 'Gross Margin of the Current Year', 'Gross Margin of the Previous Year', 'Asset Turnover Ratio of the Current Year', 'Asset Turnover Ratio of the Previous Year')
        param_count = len(params)
        net_inc, roa, cfo, long_term_debt_curr_yr, long_term_debt_prev_yr, curr_ratio_of_curr_yr, curr_ratio_of_prev_yr, shares_dil, gross_marg_curr_yr, gross_marg_prev_yr, asset_turnover_ratio_curr_yr, asset_turnover_ratio_prev_yr = [float(input(f'Enter the {params[i]}: ')) for i in range(param_count)]
        
        return {'ni': net_inc, 'roa': roa, 'cfo': cfo, 'ltd_curr': long_term_debt_curr_yr, 'ltd_prev': long_term_debt_prev_yr, 'cr_curr': curr_ratio_of_curr_yr, 'cr_prev': curr_ratio_of_prev_yr, 'share_dil': shares_dil, 'gm_curr': gross_marg_curr_yr, 'gm_prev': gross_marg_prev_yr, 'atr_curr': asset_turnover_ratio_curr_yr, 'atr_prev': asset_turnover_ratio_prev_yr}
    
    
    def calcScore(self, net_inc, roa, cfo, long_term_debt_curr_yr, long_term_debt_prev_yr, curr_ratio_of_curr_yr, curr_ratio_of_prev_yr, shares_dil, gross_marg_curr_yr, gross_marg_prev_yr, asset_turnover_ratio_curr_yr, asset_turnover_ratio_prev_yr):
        
        criteria = (net_inc > 0, roa > 0, cfo > 0, cfo > net_inc, 
                    long_term_debt_curr_yr < long_term_debt_prev_yr, curr_ratio_of_curr_yr > curr_ratio_of_prev_yr, shares_dil == 0, 
                    gross_marg_curr_yr > gross_marg_prev_yr, asset_turnover_ratio_curr_yr > asset_turnover_ratio_prev_yr)
        
        score = sum(criteria)
        
        
        
        # score = 0
        
        # Profitability Criteria-
        # if net_inc > 0:
        #     score += 1
        
        # if roa > 0:
        #     score += 1
        
        # if cfo > 0:
        #     score += 1
        
        # if cfo > net_inc:
        #     score += 1
        
        # # Leverage, Liquidity, and Source of Funds criteria-
        # if long_term_debt_curr_yr < long_term_debt_prev_yr:
        #     score += 1
        
        # if curr_ratio_of_curr_yr > curr_ratio_of_prev_yr:
        #     score += 1
        
        # if shares_dil == 0:
        #     score += 1
        
        # # Operating Efficiency criteria-
        # if gross_marg_curr_yr > gross_marg_prev_yr:
        #     score += 1
        
        # if asset_turnover_ratio_curr_yr > asset_turnover_ratio_prev_yr:
        #     score += 1
        
        
        return score
        
    def driver(self):
        params = self.getInputs()
        # net_inc, roa, cfo, long_term_debt_curr_yr, long_term_debt_prev_yr, curr_ratio_of_curr_yr, curr_ratio_of_prev_yr, shares_dil, gross_marg_curr_yr, gross_marg_prev_yr, asset_turnover_ratio_curr_yr, asset_turnover_ratio_prev_yr = params.values()
        
        score = self.calcScore(*params.values())
        
        print(f'Piotroski Score = {score} (/9)')


def main():
    ps = PiotroskiScore()
    ps.driver()

if __name__ == '__main__':
    main()


