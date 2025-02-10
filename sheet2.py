
class Agent2: #Created a class for the Agent

    def __init__(self, a, b): #Define agents position
        self.a = a
        self.b = b

    def expose_position(self): #Function to get the position of the agent
        return (self.a, self.b)

    def moveAgent(self, am, bm): #Moves an agent to a specific direction
        self.a += am
        self.b += bm


class GridWorld2:

    def __init__(self, grid_size = 5):
        self.grid_size = grid_size
        self.grid = [[0 for i in range(grid_size)] for j in range(grid_size)] #Creating a 5*5 grid world
        #Define the position of the leaf
        self.leaf = (grid_size//2, grid_size//2 + 1)
        self.agent = Agent2(grid_size//2, grid_size//2) #Position the agent
        self.addAgentAndLeaf() #Add agent by calling the method "addAgentAndLeaf"
        
    def addAgentAndLeaf(self):
        agent = Agent2
        self.a = self.grid_size//2
        self.b = self.grid_size//2
        self.grid[self.a][self.b] = 'A'

        leafPos1, leafPos2 = self.leaf
        self.grid[leafPos1][leafPos2] = "l"

        #IGNORE PLEASE
        #if (self.a, self.b) == self.leaf: #Agent and leaf
            #self.grid[self.a][self.b] = 'Al'
        #else:
            #self.grid[leafPos1][leafPos2] = "l"
            #self.grid[self.a][self.b] = 'A'
            

    def moveAgentInAllDirection(self, s):
        ##print options
    
        if s == 'west': #Moves agent west and check bouncy border
            if self.b > 0:  #Agent next to border
                self.grid[self.a][self.b] = 0   #Clear's agent current position
                self.agent.moveAgent(0,-1)  #Move agent west
                self.a, self.b = self.agent.expose_position() #Gets the new position
            
            else:   #Bounce agent
                print("Agent senses a border")
        


        elif s == 'east': #Moves agent east and check bouncy border
            
            if self.b < 4:  #Agent next to border
                self.grid[self.a][self.b] = 0   #Clear's agent current position
                self.agent.moveAgent(0,1)  #Move agent east
                self.a, self.b = self.agent.expose_position() #Gets the new position

            else:   #Bounce agent
                print("Agent senses a border")
        

        elif s == 'north': #Moves agent east and check bouncy border
            if self.a > 0:  #Agent next to border
                self.grid[self.a][self.b] = 0   #Clear's agent current position
                self.agent.moveAgent(-1,0)  #Move agent east
                self.a, self.b = self.agent.expose_position() #Gets the new position
            
            else:   #Bounce agent
                print("Agent senses a border")
        

        elif s == 'south': #Moves agent east and check bouncy border
            if self.a < 4:  #Agent next to border
                self.grid[self.a][self.b] = 0   #Clear's agent current position
                self.agent.moveAgent(1,0)  #Move agent east
                self.a, self.b = self.agent.expose_position() #Gets the new position
            
            else:   #Bounce agent
                print("Agent senses a border")
        
        ##Update the grid with the agent's new position
        if (self.a, self.b) == self.leaf: #Agent and leaf
            self.grid[self.a][self.b] = 'Al'
        else:
            self.grid[self.a][self.b] = 'A'
            self.leaf
        
        #Ensure the leaf remains in its position if the Agent leaves or
        # is not on the leaf coordinate
        leafPos1, leafPos2 = self.leaf
        if self.grid[leafPos1][leafPos2] != "Al": #if Agent is not on leaf
            self.grid[leafPos1][leafPos2] = 'l' #Keeps the leaf in its place
            

    def leafObstacle(self, s):
        
        if s == 'west': #Move agent west and check bouncy border
            if self.b > 0:  #Agent next to border?
                new_a, new_b = self.a, self.b - 1
                if self.grid[new_a][new_b] == 'l': #Check if leaf is in the next cell
                        
                        self.grid[new_a][new_b] = 0   #Clear leaf current position
                        self.grid[new_a][new_b - 1] = "l" #Move leaf
                        self.grid[self.a][self.b] = 0 #clear agent current position
                        self.grid[self.a][self.b -1 ] = 'A' #Move agent
                        
                else:
                    self.moveAgentInAllDirection(s)  #Call moveAgentInAllDirection method to move agent
                                
            else: #Bounce agent on border
                print("Agent senses a border")
            
        ######Moves agent and leaf East
        if s == 'east': #Move agent west and check bouncy border
            if self.b < 4:  #Agent next to border?
                new_a, new_b = self.a, self.b + 1
                if self.grid[new_a][new_b] == 'l': #Check if leaf is in the next cell
                        
                        self.grid[new_a][new_b] = 0   #Clear leaf current position
                        self.grid[new_a][new_b + 1] = "l" #Move leaf
                        self.grid[self.a][self.b] = 0 #clear agent current position
                        self.grid[self.a][self.b + 1 ] = 'A' #Move agent
                        
                else:
                    self.moveAgentInAllDirection(s)  #Call moveAgentInAllDirection method to move agent
                                
            else: #Bounce agent on border
                print("Agent senses a border")

        ######Moves agent and leaf North
        if s == 'north': #Move agent west and check bouncy border
            if self.a > 0:  #Agent next to border?
                new_a, new_b = self.a - 1, self.b
                if self.grid[new_a][new_b] == 'l': #Check if leaf is in the next cell
                        
                        self.grid[new_a][new_b] = 0   #Clear leaf current position
                        self.grid[new_a - 1][new_b] = "l" #Move leaf
                        self.grid[self.a][self.b] = 0 #clear agent current position
                        self.grid[self.a - 1][self.b] = 'A' #Move agent
                        
                else:
                    self.moveAgentInAllDirection(s)  #Call moveAgentInAllDirection method to move agent
                                
            else: #Bounce agent on border
                print("Agent senses a border")

        ######Moves agent and leaf South
        if s == 'south': #Move agent west and check bouncy border
            if self.a < 4:  #Agent next to border?
                new_a, new_b = self.a + 1, self.b
                if self.grid[new_a][new_b] == 'l': #Check if leaf is in the next cell
                        
                        self.grid[new_a][new_b] = 0   #Clear leaf current position
                        self.grid[new_a + 1][new_b] = "l" #Move leaf
                        self.grid[self.a][self.b] = 0 #clear agent current position
                        self.grid[self.a + 1][self.b] = 'A' #Move agent
                   
                else:
                    self.moveAgentInAllDirection(s)  #Call moveAgentInAllDirection method to move agent
                                
            else: #Bounce agent on border
                print("Agent senses a border")
    
    

    def print_grid(self): #This print each list on a new line rather on a straight long list
        for newLine in self.grid:
            print(newLine)


        
        
################################################
###
world2 = GridWorld2() #Initialise GridWorld2

#Create grid
print("******New World Grid******\n")
world2.print_grid() #Prints the Grid world

#Moves agent west
print("\n\n******Move agent West*******")
world2.moveAgentInAllDirection("west")
world2.print_grid() #Prints the Grid world

#Moves agent East
print("\n\n******Move agent East*******")
world2.moveAgentInAllDirection("east")
world2.print_grid() #Prints the Grid world

#Moves agent East
print("\n\n******Move agent East*******") #Move agent east again to see if it's at the same position as leaf
world2.moveAgentInAllDirection("east")
world2.print_grid() #Prints the Grid world

#Moves agent North
print("\n\n******Move agent North*******")
world2.moveAgentInAllDirection("north")
world2.print_grid() #Prints the Grid world

#Moves agent South
print("\n\n******Move agent South*******")
world2.moveAgentInAllDirection("south")
world2.print_grid() #Prints the Grid world

#Moves agent South
print("\n\n******Move agent South*******") #Move south again to ensure leaf remains in its position
world2.moveAgentInAllDirection("south")
world2.print_grid() #Prints the Grid world


print("\n\n\n\n**************Moving Agent anf Leaf*****************")
#Moves Agent and leaf west
print("\n\n******Move agent&Leaf West*******")
world2.leafObstacle('west')
world2.print_grid() #Prints the Grid world

#Moves Agent and leaf east
print("\n\n******Move agent&Leaf East*******")
world2.leafObstacle('east')
world2.print_grid() #Prints the Grid world

#Moves Agent and leaf east again
print("\n\n******Move agent&Leaf East*******")
world2.leafObstacle('east')
world2.print_grid() #Prints the Grid world

#Moves Agent and leaf North
print("\n\n******Move agent&Leaf North*******")
world2.leafObstacle('north')
world2.print_grid() #Prints the Grid world

#Moves Agent and leaf South
print("\n\n******Move agent&Leaf South*******")
world2.leafObstacle('south')
world2.print_grid() #Prints the Grid world
