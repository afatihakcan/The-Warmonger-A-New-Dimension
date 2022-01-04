#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 21:29:56 2021

@author: Ahmet Fatih Akcan
@contact: afatihakcan@protonmail.com
"""

import sys #to catch the lines belong to errors
# =============================================================================
class Faction:
    def __init__(self, name="just a faction", unit_num = 50, attack_point = 50, health_point = 150, reg_num = 10):
        self.name = name #name of initialized faction
        self.unit_num = unit_num 
        self.attack_point = attack_point
        self.health_point = health_point
        self.reg_num = reg_num #regeneration num
        self.total_health = self.unit_num * self.health_point
        self.is_alive = True #alive flag
        
    def AssgnEnemies(self, first_enemy, second_enemy):
        self.first_enemy = first_enemy 
        self.second_enemy = second_enemy
        
    def PerformAttack(self):
        return self.unit_num * self.attack_point / 100
    
    def ReceiveAttack(self, damage):
        self.unit_num -= damage
        

    def PurchaseWeapons(self, increase_attack, profit):
        self.attack_point += increase_attack #purchasing weapons leads to increase the attack point
        return profit
        
        
    def PurchaseArmors(self, increase_health, profit):
        self.health_point += increase_health #purchasing armors leads to increase the health point
        return profit
    
    def Print(self):
        info=f"""
|\u0305  Faction Name         : {self.name}
|  Status               : {'Alive' if self.is_alive == True else 'Defeated'}
|  Number of Units      : {self.unit_num}
|  Attack Point         : {self.attack_point}
|  Health Point         : {self.health_point}
|  Unit Regen Number    : {self.reg_num}
|\u005f Total Faction Health : {self.total_health}
        """
        print(info)
        
    def EndTurn(self): # to be called at the end of the day
        self.unit_num += self.reg_num
        if self.unit_num <= 0: self.unit_num = 0; self.is_alive = False 
        self.total_health = self.unit_num * self.health_point
# =============================================================================
        
    
# =============================================================================
class Orcs(Faction):
    def __init__(self, name = "just orcs"):
        super().__init__(name) #inheritance from class Faction
    
    def PerformAttack(self):
        if (self.first_enemy.is_alive and not self.second_enemy.is_alive): #first_enemy: Dwarves, second_enemy: Elves
            self.first_enemy.ReceiveAttack(super().PerformAttack(), 'Orcs')
        
        elif (not self.first_enemy.is_alive and self.second_enemy.is_alive):
            self.second_enemy.ReceiveAttack(super().PerformAttack(), 'Orcs')
            
        elif (self.first_enemy.is_alive and self.second_enemy.is_alive):
            self.first_enemy.ReceiveAttack(super().PerformAttack()*0.3, 'Dwarves')
            self.first_enemy.ReceiveAttack(super().PerformAttack()*0.7, 'Dwarves')
            
        else:
            raise Exception(f"SORRY, CHECK YOUR CODE MORUK!! in line: {sys._getframe().f_lineno}")
        
    
    def ReceiveAttack(self, damage, obj):
        if obj == 'Elves':
            super().ReceiveAttack(0.75*(damage/self.health_point))
        elif obj == 'Dwarves':
            super().ReceiveAttack(0.8*(damage/self.health_point))
        else:
            raise Exception(f"SORRY, CHECK YOUR CODE MORUK!! in line: {sys._getframe().f_lineno}")
            
    def PurchaseWeapons(self, weapon_bought):
        return (super().PurchaseWeapons(2*weapon_bought, 20*weapon_bought))
    
    def PurchaseArmors(self, armor_bought):
        return (super().PurchaseArmors(3*armor_bought, 1*armor_bought))
    
    def Print(self):
        print("Stop running, you'll only die tired!")
        super().Print()
# =============================================================================
        


# =============================================================================
class Dwarves(Faction):
    def __init__(self, name = "just dwarves"):
        super().__init__(name) #inheritance from class Faction
    
    
    def PerformAttack(self): # first_enemy: Orcs, second_enemy: Elves
        if (self.first_enemy.is_alive and not self.second_enemy.is_alive):
            self.first_enemy.ReceiveAttack(super().PerformAttack(), 'Dwarves')
        
        elif (not self.first_enemy.is_alive and self.second_enemy.is_alive):
            self.second_enemy.ReceiveAttack(super().PerformAttack(), 'Dwarves')
            
        elif (self.first_enemy.is_alive and self.second_enemy.is_alive):
            self.first_enemy.ReceiveAttack(super().PerformAttack()/2, 'Dwarves')
            self.second_enemy.ReceiveAttack(super().PerformAttack()/2, 'Dwarves')
            
        else:
            raise Exception(f"SORRY, CHECK YOUR CODE MORUK!! in line: {sys._getframe().f_lineno}")
            
    
    def ReceiveAttack(self, damage, obj):
        super().ReceiveAttack(damage/self.health_point)
        

    def PurchaseWeapons(self, weapon_bought):
        return (super().PurchaseWeapons(weapon_bought, 10*weapon_bought))
    
    
    def PurchaseArmors(self, armor_bought):
        return (super().PurchaseArmors(2*armor_bought, 3*armor_bought))
    
    
    def Print(self):
        print("Taste the power of our axes!")
        super().Print()
# =============================================================================


# =============================================================================
class Elves(Faction):
    def __init__(self, name = "just elves"):
        super().__init__(name) #inheritance from class Faction
        
    def PerformAttack(self): #first_enemy: Orcs, second_enemy: Dwarves
        if (self.first_enemy.is_alive and not self.second_enemy.is_alive):
            self.first_enemy.ReceiveAttack(super().PerformAttack(), 'Elves')
        
        elif (not self.first_enemy.is_alive and self.second_enemy.is_alive):
            self.second_enemy.ReceiveAttack(super().PerformAttack()*1.5, 'Elves')
            
        elif (self.first_enemy.is_alive and self.second_enemy.is_alive):
            self.first_enemy.ReceiveAttack(super().PerformAttack()*0.6, 'Elves')
            self.second_enemy.ReceiveAttack(super().PerformAttack()*0.4*1.5, 'Elves')
            
        else:
            raise Exception(f"SORRY, CHECK YOUR CODE MORUK!! in line: {sys._getframe().f_lineno}")
            
            
    def ReceiveAttack(self, damage, obj):
        if obj == 'Orcs':
            super().ReceiveAttack(damage/self.health*1.25)
        
        elif obj == 'Dwarves':
            super().ReceiveAttack(damage/self.health_point*0.75)
            
        else:
            raise Exception(f"SORRY, CHECK YOUR CODE MORUK!! in line: {sys._getframe().f_lineno}")


    def PurchaseWeapons(self, weapon_bought):
        return(super().PurchaseWeapons(2*weapon_bought, 15*weapon_bought))
        
    def PurchaseArmors(self, armor_bought):
        return(super().PurchaseArmors(4*armor_bought, 5*armor_bought))
        
    def Print(self):
        print("You cannot reach our elegance.")
        super().Print()
# =============================================================================


class Merchant:
    def __init__(self, start_weapon=10, start_armor=10):
        self.start_weapon = start_weapon
        self.start_armor = start_armor
        self.EndTurn()
        self.revenue = 0
        
    def AssgnFaction(self, f, s, t):
        self.first_faction = f #Orcs
        self.second_faction = s #Dwarves
        self.third_faction = t #Elves
        
    def SellWeapons(self, to_whom, weapons_to_sell):
        if to_whom == 'Orcs': to_whom = self.first_faction
        elif to_whom == 'Dwarves': to_whom = self.second_faction
        elif to_whom == 'Elves': to_whom = self.third_faction
        else: raise Exception(f"SORRY, CHECK YOUR CODE MORUK!! in line: {sys._getframe().f_lineno}")
        
        if not to_whom.is_alive: print("The faction you want to sell weapons is dead!")
        else:
            if weapons_to_sell > self.weapon_num: 
                print("You try to sell more weapons than you have in possession")
                return False
            
            else:
                self.revenue += to_whom.PurchaseWeapons(weapons_to_sell)
                print("Weapons sold!")
                self.weapon_num -= weapons_to_sell
                return True
        
        
    def SellArmors(self, to_whom, armors_to_sell):
        if to_whom == 'Orcs': to_whom = self.first_faction
        elif to_whom == 'Dwarves': to_whom = self.second_faction
        elif to_whom == 'Elves': to_whom = self.third_faction
        else: raise Exception(f"SORRY, CHECK YOUR CODE MORUK!! in line: {sys._getframe().f_lineno}")
        
        if not to_whom.is_alive: print("The faction you want to sell armors is dead!")
        else:
            if armors_to_sell > self.armor_num: 
                print("You try to sell more armors than you have in possession")
                return False
            
            else:
                self.revenue += to_whom.PurchaseArmors(armors_to_sell)
                print("Armors sold!")
                self.armor_num -= armors_to_sell
                return True
            
    
    def EndTurn(self): # need to be called at the init and the end of the day
        self.weapon_num = self.start_weapon
        self.armor_num = self.start_armor
        


# DİKKAT AŞAĞISI ŞAMPİYONLAR LİGİ GİBİ!
class DümendenUI:
    is_shutdown = False #not only a kinda rospy.is_shutdown() but also a flag
    
    def __init__(self):
        player_name = str(input("Welcome to the Game!, Please Enter Your Name: "))
        if player_name == 'quit': 
            self.is_shutdown = False
            self.is_newgame = False
            return
        else : 
            print(f"Welcome {player_name}!")
            self.Menus = self.MenusClass(player_name) #create an object from class MenusClass which can be seen below
            
            
    def __newgame(self):
        self.is_newgame = True #flag to start a new game
        return 0
    
    def __quit(self):
        self.is_shutdown = True #flag to quit game
        return -1
        
    class MenusClass:
        def __init__(self, player_name = 'Adı yok namı var: PALA'):
#----------------------menu texts that will be shown in menus----------------------
            self.main_menu_text= f"""
1) See the information of Factions
2) Sell Weapons
3) Sell Armors
4) End the Day
5) End the Game
6) Quit
            """
        
            self.info_menu_text = f"""
1) Orcs
2) Dwarves
3) Elves
4) Back
5) Quit
            """
       
            self.sell_menu_text = f"""
1) To Orcs
2) To Dwarves
3) To Elves
4) Back
5) Quit
            """
#----------------------------------------------------------------------------------------
            
#----------------------menu decision mechanisms----------------------
        def main_menu(self):
            choice = str(input(self.main_menu_text))
            if choice == '1':
                if self.info_menu() == -1: return -1
            elif choice == '2':
                if self.weapon_menu() == -1: return -1
            elif choice == '3':
                if self.armor_menu() == -1: return -1
            elif choice == '4':
                return 1
            elif choice == '5':
                return 0
            elif choice == '6':
                return -1
            
        
        def info_menu(self):
            choice = str(input(self.info_menu_text))
            if choice == '1':
                Orcs_obj.Print()
            elif choice == '2':
                Dwarves_obj.Print()
            elif choice == '3':
                Elves_obj.Print()
            elif choice == '4':
                return
            elif choice == '5':
                return -1 #quit
            
        def weapon_menu(self):
            choice = str(input(self.sell_menu_text))
            if choice == '5':
                return -1
            elif choice == '4':
                return
            elif choice == '1' or choice == '2' or choice == '3':
                try:
                    num = int(input("Number of weapons you want to sell: "))
                except ValueError:
                    print("wrong input!")
                    return
                
                if choice == '1':
                    to_whom = 'Orcs'
                elif choice == '2':
                    to_whom = 'Dwarves'
                else :
                    to_whom = 'Elves'
                
                if not Merchant_obj.SellWeapons(to_whom, num):
                  return
              
            else: print(f"there is no choice {choice}!")
        
        def armor_menu(self):
            choice = str(input(self.sell_menu_text))
            if choice == '5':
                return -1
            elif choice == '4':
                return
            elif choice == '1' or choice == '2' or choice == '3':
                try:
                    num = int(input("Number of armors you want to sell: "))
                except ValueError:
                    print("wrong input!")
                    return
                
                if choice == '1':
                    to_whom = 'Orcs'
                elif choice == '2':
                    to_whom = 'Dwarves'
                else :
                    to_whom = 'Elves'
                
                if not Merchant_obj.SellArmors(to_whom, num):
                  return
              
            else: print(f"there is no choice {choice}!")
#----------------------------------------------------------------------------------------
        
    def RunGame(self): #Run menus
        ret = self.Menus.main_menu()
        if ret == -1: return self.__quit()
        elif ret == 0: return self.__newgame()
        else: return ret
        

class Main: # Class that acts like a game engine
    def __init__(self):
        self.gamepy = DümendenUI() #bi rospy değil ama boyun da eğmez
        self.days = 1
        global Orcs_obj #global Orcs object
        Orcs_obj = Orcs()
        global Dwarves_obj #global Dwarves object
        Dwarves_obj = Dwarves()
        global Elves_obj
        Elves_obj = Elves() #global Elves object
        global Merchant_obj #global Merchant object
        Merchant_obj = Merchant()
        
        Orcs_obj.AssgnEnemies(Dwarves_obj, Elves_obj) #assign enemies to faction Orcs
        Dwarves_obj.AssgnEnemies(Orcs_obj, Elves_obj) #assign enemies to faction Dwarves
        Elves_obj.AssgnEnemies(Orcs_obj, Dwarves_obj) #assign enemies to faction Elves
        
        Merchant_obj.AssgnFaction(Orcs_obj, Dwarves_obj, Elves_obj) #assign factions to the Merchant
    
    def EndTurn(self): #updates the factions' and the merchant's informations
        Orcs_obj.EndTurn()
        Dwarves_obj.EndTurn()
        Elves_obj.EndTurn()
        Merchant_obj.EndTurn()
        
    def performAttacks(self): #hesaplaşma vakti :)
        Orcs_obj.PerformAttack()
        Dwarves_obj.PerformAttack()
        Elves_obj.PerformAttack()
    
    def Run(self): # Runs the game
        while not self.gamepy.is_shutdown:
            ret = self.gamepy.RunGame()
            if ret == -1 or ret == 0: break # -1 means quit game, 0 means new game
            elif ret == 1: # 1 means new day
                self.EndTurn() #update infos
                self.performAttacks() #hesaplaşma vakti :)
                print(f"gün {self.days} completed")
                self.days += 1
            else: print(f"Day {self.days} continues..")
                
            

if __name__ == '__main__':
    while(1):
        Game = Main() #creates an game object from the Class which actually runs the game
        Game.Run() #RUN!
        
        if Game.gamepy.is_shutdown == True: #oysa herkes öldürür sevdiğini..
            break
        elif Game.gamepy.is_newgame == True:
            #deletes all objects belongs to the game which is wanted to be finished
            del Game
            del Orcs_obj
            del Dwarves_obj
            del Elves_obj
            del Merchant_obj
            print("You better play better this time..")
        else: 
            print("FATAL ERROR SAĞLAM PATLADIN MORUK!") #thankfully never happened (1 yanlış bütün doğruları götürür)
            break
            
    print("Thank you for playing!")
    