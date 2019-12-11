Conventional_Loan = ['Conventional Loan', 600, 30000]
Conforming_Loan = ['Conforming Loan', 500, 10000]
NonConforming_Loan = ['Non-Conforming Loan', 650, 10000]
Secured_Loan = ['Secured Loan', 650, 20000]
Unsecured_Loan = ['Unsecured Loan', 500, 30000]
Openended_Loan = ['Open-ended Loan', 400, 5000]
Closeended_Loan = ['Close-ended Loan', 450, 5000]
"""these variables set the initial prerequisits to qualify for the loans offered by NicksLoans"""


class NicksLoans():
    """this class contains all information for the bank NicksLoans.
    
    Attributes:
        name (str): Name of applicant
        date (str): Date of application
        annual_income (int): Most recent known annual income of applicant in US dollars, without commas
        loan_type (str): Type of loan requested on app
        credit_score (int): Most recent known credit score of applicant, from 300-850, without commas
    """
    
    loan_status = 'To Be Determined'
    """this class attribute predetermines the status of the loan"""

    loan_offers = ['Conventional Loan', 'Conforming Loan', 'Non-Conforming Loan',
                 'Secured Loan', 'Unsecured Loan', 'Open-ended Loan', 'Close-ended Loan']
    """this class attribute determines which types of loans are offered at NicksLoans"""

    
    def __init__(self, name, date, annual_income, 
                 loan_type, credit_score):
        """The constructor for NicksLoans class.
    
        Parameters:
            name (str): Name of applicant
            date (str): Date of application
            annual_income (int): Most recent known annual income of applicant in US dollars, without commas
            loan_type (str): Type of loan requested on app
            credit_score (int): Most recent known credit score of applicant, from 300-850, without commas
        """
       
        self.name = name
        self.date = date
        self.annual_income = annual_income
        self.loan_type = loan_type
        self.credit_score = credit_score
       
        
    def summary(self):  
        """The function gives a summary for a NicksLoans application with the given parameters
    
        Parameters:
            name (str): Name of applicant
            date (str): Date of application
            annual_income (int): Most recent known annual income of applicant in US dollars, without commas
            loan_type (str): Type of loan requested on app
            credit_score (int): Most recent known credit score of applicant, from 300-850, without commas
            
        Returns:
            summary (str): A string that clearly states a summary of the applicant's information and application information.
        """
        
        print('On', self.date, self.name, 'applied for a', self.loan_type, 'with a credit score of', self.credit_score, 
              'and an annual income of $', self.annual_income)
         
            
    def offers(self):
        """this function provides a summary of the loans offered at NicksLoans
        
        Parameters:
            loan_offers (str): Types of loans offered by NicksLoans
            
        Returns:
            offers (str): A string that clearly states the loans offered by NicksLoans.
        """
            
        print('We offer a variety of options such as a', self.loan_offers[0:-2], 'or a', 
              self.loan_offers[-1])
        
        
    def app_run(self):
        """this function compares the applicant's information with the prerequisits for loans offered at this bank
           and approves or denies them accordingly
           
           Parameters:
            annual_income (int): Most recent known annual income of applicant in US dollars, without commas
            loan_type (str): Type of loan requested on app
            credit_score (int): Most recent known credit score of applicant, from 300-850, without commas
            
        Returns:
            loan_status (str): A string that updates the loan status variable to approved or denied based on the comparision.
        """
           
        if self.credit_score < loan_type[1]:
                
            loan_status = 'Denied'
                
        elif self.annual_income < loan_type[2]:
                
            loan_status = 'Denied'
                
        elif self.credit_score >= loan_type[1] and self.annual_income >= loan_type[2]:
                
            loan_status = 'Approved, congratulations'
                
        return loan_status
