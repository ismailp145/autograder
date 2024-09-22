import os
import sys
import importlib
import csv

def main():
    
    submissions_dir = '/Users/ismail/Desktop/GRADING/Fall-2024/CSC-243/Assignments/A2'
    sys.path.insert(0, submissions_dir)

    
    with open('resultsA2.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([
            'Filename',
            'portfolio_intersection1',
            'portfolio_intersection2',
            'extract_stock_price1',
            'extract_stock_price2',
            'extract_stock_price3',
            'extract_stock_price4',
            'analyze_fund_description1',
            'analyze_fund_description2',
            'analyze_fund_description3',
            'analyze_fund_description4',
            'generate_trade_ticker1',
            'generate_trade_ticker2',
            'generate_trade_ticker3',
            'count_trade_frequency1',
            'count_trade_frequency2',
            'count_trade_frequency3'
        ])
    for filename in os.listdir(submissions_dir):

        if filename.endswith('.py'):
            try:              
                current_student = importlib.import_module(filename[:-3])
                row = [current_student.__name__]   
                                
                if hasattr(current_student, 'portfolio_intersection'):
                    pi1 = current_student.portfolio_intersection(['ABSE', 'APPL', 'NVID', 'MSFT'], ['MSFT', 'TSLA', 'XCOM', 'APPL'])
                    pi2 = current_student.portfolio_intersection(['ABSE', 'APPL', 'NVID', 'MSFT'], ['TSLA', 'XCOM', 'EXXO', 'OLTP'])
                    row.extend([pi1, pi2])

                if hasattr(current_student, 'extract_stock_price'):

                    esp1 = current_student.extract_stock_price('APPL;Trading above cap;180;SELL;do not short')
                    esp2 = current_student.extract_stock_price('150;MSFT;BUY;short;Revisit history of stock price for later algos')
                    esp3 = current_student.extract_stock_price('APPL;Trading above cap;179.99;SELL;do not short')
                    esp4 = current_student.extract_stock_price('APPL;Trading above cap;BUY;do not short')
                    row.extend([esp1, esp2, esp3, esp4])

                if hasattr(current_student, 'analyze_fund_description'):
                    afd1 = current_student.analyze_fund_description("MOON is the hottest and most splendiferous new cryptocurrency on the market do not delay in purchasing a googleplex of shares in it immediately", 5)
                    afd2 = current_student. analyze_fund_description("MOON is the hottest and most splendiferous new cryptocurrency on the market do not delay in purchasing a googleplex of shares in it immediately", 14)
                    afd3 = current_student.analyze_fund_description("MOON is the hottest and most splendiferous new cryptocurrency on the market do not delay in purchasing a googleplex of shares in it immediately", 15)
                    afd4 = current_student.analyze_fund_description("MOON is the hottest and most splendiferous new cryptocurrency on the market do not delay in purchasing a googleplex of shares in it immediately", -1)
                    row.extend([afd1, afd2, afd3, afd4])

                if hasattr(current_student, 'generate_trade_ticker'):
                    gtt1 = current_student.generate_trade_ticker('APPL')
                    gtt2 = current_student.generate_trade_ticker('msft')
                    gtt3 = current_student.generate_trade_ticker('')
                    row.extend([gtt1, gtt2, gtt3])

                if hasattr(current_student, 'count_trade_frequency'):
                    ctf1 = current_student.count_trade_frequency('APPL BUY;MSFT BUY;MSFT SELL;TSLA SELL;APPL BUY; APPL SELL', 'appl')
                    ctf2 = current_student.count_trade_frequency('Appl BUY;Msft BUY;Msft SELL;TSLA SELL;Appl BUY; Appl SELL', 'MSFT')
                    ctf3 = current_student.count_trade_frequency('Appl BUY;Msft BUY;Msft SELL;TSLA SELL;Appl BUY; Appl SELL', '') 
                    row.extend([ctf1, ctf2, ctf3])
                
                writer.writerow(row)

            except Exception as e:
                print(f"Error importing or running {filename}: {e}")
                
if __name__ == "__main__":
    main()