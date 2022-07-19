''' Standard Credit Rating '''

'''

    Piotroski/FAB Score - Rating
    0 - Unrated
    1 - Unrated
    2 - BB and below
    3 - BB and below
    4 - BBB
    5 - BBB
    6 - A
    7 - AA
    8 - AA
    9 - AAA
    10(FAB) – AAA

'''


class StandardCreditRating:
    def getScoreType(self):
        try:
            score_type = input('Please Enter the Score Type(Piotroski Score(P) or FAB Score(F)): ')
        except:
            print('Oops! Not a Valid Score Type(Piotroski Score or FAB Score).')
            return
        return score_type
    
    def getScore(self, score_type = 'p'):
        try:
            if score_type.lower() in ('piotroski score', 'piotroski', 'p'):
                score = int(input('Please Enter the Piotroski Score(0 - 9): '))
            
            elif score_type.lower() in ('fab score', 'fab', 'f'):
                score = int(input('Please Enter the FAB Score(0 - 10): '))
            return score
        except:
            return None
            # if score_type.lower() in ('piotroski score', 'piotroski', 'p'):
            #     print('Whoops! Not a Valid Value for Piotroski Score (0 - 9)')
            
            # elif score_type.lower() in ('fab score', 'fab', 'f'):
            #     print('Whoops! Not a Valid Value for FAB Score (0 - 10)')
        
        # else:
        # return score
    
    def getRating(self, score, score_type = 'p'):
        if score == 10:
            if score_type.lower() in ('fab score', 'fab', 'f'):
                rating = 'AAA'
            else:
                rating = None
        
        elif score == 9:
            rating = 'AAA'
        
        elif score in (7, 8):
            rating = 'AA'
        
        elif score == 6:
            rating = 'A'
        
        elif score in (4, 5):
            rating = 'BBB'
        
        elif score in (2, 3):
            rating = 'BB and below'
        
        elif score in (0, 1):
            rating = 'Unrated'
        
        else:
            rating = None
        
        return rating
    
    def driver(self):
        score_type = self.getScoreType()
        
        if score_type.lower() not in ('piotroski score', 'piotroski', 'p', 'fab score', 'fab', 'f'):
            print('Oops! Not a Valid Score Type(Piotroski or FAB).')
            return
        
        score = self.getScore(score_type)
        
        
        rating = self.getRating(score, score_type)
        
        if rating != None:
            if score_type.lower() in ('piotroski score', 'piotroski', 'p'):
                print(f'Standard Credit Rating(Piotroski): {rating}')
            
            else:
                print(f'Standard Credit Rating(FAB): {rating}')
        else:
            if score_type.lower() in ('piotroski score', 'piotroski', 'p'):
                print('Whoops! Not a Valid value for Piotroski Score (0 - 9).')
                
            else:
                print('Whoops! Not a Valid value for FAB Score(0 - 10).')

def main():
    stdcr = StandardCreditRating()
    stdcr.driver()

if __name__ == '__main__':
    main()


