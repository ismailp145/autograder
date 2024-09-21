import os
import sys
import importlib


def main():

    submissions_dir = '/Users/ismail/Desktop/GRADING/Fall-2024/CSC-243/Assignments/A2'
    sys.path.insert(0, submissions_dir)

    for filename in os.listdir(submissions_dir):

        if filename.endswith('.py'):
            try:              
                current_student = importlib.import_module(filename[:-3])
                                
                if hasattr(current_student, 'portfolio_intersection'):
                    pi1 = current_student.portfolio_intersection(['ABSE', 'APPL', 'NVID', 'MSFT'], ['MSFT', 'TSLA', 'XCOM', 'APPL'])
                    pi2 = current_student.portfolio_intersection(['ABSE', 'APPL', 'NVID', 'MSFT'], ['TSLA', 'XCOM', 'EXXO', 'OLTP'])


                if hasattr(current_student, 'extract_stock_price'):

                    esp1 = current_student.extract_stock_price('APPL;Trading above cap;180;SELL;do not short')
                    esp2 = current_student.extract_stock_price('150;MSFT;BUY;short;Revisit history of stock price for later algos')
                    esp3 = current_student.extract_stock_price('APPL;Trading above cap;179.99;SELL;do not short')
                    esp4 = current_student.extract_stock_price('APPL;Trading above cap;BUY;do not short')

                if hasattr(current_student, 'analyze_fund_description'):
                    afd1 = current_student.analyze_fund_description("MOON is the hottest and most splendiferous new cryptocurrency on the market do not delay in purchasing a googleplex of shares in it immediately", 5)
                    afd2 = current_student. analyze_fund_description("MOON is the hottest and most splendiferous new cryptocurrency on the market do not delay in purchasing a googleplex of shares in it immediately", 14)
                    afd3 = current_student.analyze_fund_description("MOON is the hottest and most splendiferous new cryptocurrency on the market do not delay in purchasing a googleplex of shares in it immediately", 15)
                    afd4 = current_student.analyze_fund_description("MOON is the hottest and most splendiferous new cryptocurrency on the market do not delay in purchasing a googleplex of shares in it immediately", -1)

                if hasattr(current_student, 'generate_trade_ticker'):
                    gtt1 = current_student.generate_trade_ticker('APPL')
                    gtt2 = current_student.generate_trade_ticker('msft')
                    gtt3 = current_student.generate_trade_ticker('')


                if hasattr(current_student, 'count_trade_frequency'):
                    ctf1 = current_student.count_trade_frequency('APPL BUY;MSFT BUY;MSFT SELL;TSLA SELL;APPL BUY; APPL SELL', 'appl')
                    ctf2 = current_student.count_trade_frequency('Appl BUY;Msft BUY;Msft SELL;TSLA SELL;Appl BUY; Appl SELL', 'MSFT')
                    ctf3 = current_student.count_trade_frequency('Appl BUY;Msft BUY;Msft SELL;TSLA SELL;Appl BUY; Appl SELL', '')

                csv_file = open('resultsA2.csv', 'w')
                csv_file.write('''Filename,
                               portfolio_intersection1,
                               portfolio_intersection2,

                               extract_stock_price1,
                               extract_stock_price2,
                               extract_stock_price3,
                               extract_stock_price4,
                               
                               analyze_fund_description1,
                               analyze_fund_description2,
                               analyze_fund_description3,
                               analyze_fund_description4,

                               generate_trade_ticker1,
                               generate_trade_ticker2,
                               generate_trade_ticker3,

                               count_trade_frequency1,
                               count_trade_frequency2, 
                               count_trade_frequency3, 

                               \n''')
                csv_file.write(f'{current_student.__name__},\n')
                # fill in with other test cases and label the headers with the test case numbers and if there was a pass or fail. 
                csv_file.close()
            
            except Exception as e:
                print(f"Error importing or running {filename}: {e}")






        

if __name__ == "__main__":
    main()