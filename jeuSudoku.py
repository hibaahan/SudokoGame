def verifierLigne(grille, row, num):
    '''
        (list, int, int) -> Bool
        Vérifier si la case à ajouter n'existe pas sur la ligne.
        Preconditions: grille est une reference a une matrice 9x9 qui contient déja des nombres de 1 à 9
    '''
    # A COMPLETER
    
    resultat=True
    if num in grille[row]:
        resultat=False
    return(resultat)    
            
    

def verifierCol(grille, col, num):
    '''
            (list, int, int) -> Bool
            Vérifier si la case à ajouter n'existe pas sur la colonne.
            Preconditions: grille est une reference a une matrice 9x9 qui contient déja des nombres de 1 à 9
    '''
    # A COMPLETER
    l_col=[]
    for row in grille:
        l_col.append(row[col])
    resultat=True
    if num in l_col:
        resultat=False
    return(resultat)    
    

def verifierSousGrille(grille, row, col, num):
    '''
            (list, int, int) -> Bool
            Vérifier si la case à ajouter n'existe pas sur la sous-grille.
            Preconditions: grille est une reference a une matrice 9x9 qui contient déja des nombres de 1 à 9
    '''

    # A COMPLETER
    row=row-row%3
    col=col-col%3
    resultat=True
    for i in range(3):
        for j in range(3):
            if grille[row + i][col + j] == num:
                resultat= False
    return(resultat)            

              
            
def verifierGagner(grille):
    '''(list) ->  bool
    * Preconditions: grille est une reference a une matrice 9x9 qui contient de nombres de 1 à 9
    * Verifie si la grille est completement remplie.
    '''
    
    # A COMPLETER
    resultat=True
    for row in grille:
        if 0 in row :
            resultat=False
    return(resultat)        
            


    
    
        
            
        
        
               
       
  
def verifierValide(grille, row, col, num):
   ''' (list, int, int, int) ->  bool
   * verifie si le nombre proposé est bon sur la ligne et colonne et la sous-grille donné en parametre.
   * Preconditions: tab est une reference a une matrice 9 x 9 qui contient des chiffres entre 1 et 9
   '''
   
   # A COMPLETER
   return(verifierLigne(grille, row, num) and verifierCol(grille, col, num) and verifierSousGrille(grille, row , col , num))








   
   

