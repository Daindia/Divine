print('''User is required to move through a maze to get to the other side.
User will not get to see the maze but will be provided with instructions to
move through the maze.
There is three scenarios available: Haunted house, Jungle, and Medieval Times.
Type A for Haunted House
B for Jungle
C for Medieval Times.''')
sce = input('')                      #User is required to pick a scene

while sce != 'A' and sce != 'a' and sce != 'B' and sce != 'b' and sce != 'C' and sce != 'c':
    sce = input('Invalid selection: ')#If user's choice is invalid, the prompt will keep repeating

if sce == 'A' or sce == 'a':          #If the user picked the haunted house, run this code block.
    print('''Welcome to the Haunted house!
    To move forward enter F, to move left enter L, to move right enter R.
    Once you made your choice there is no going back!
    It is forbidden for you to travel the same path twice!''')#The narration.
    dir = input('Enter F to enter the house: ')
                                      #Prompt the user to take action moving into the house.
    while dir != 'F' and dir != 'f':  #Prompts the user to retry, if the input is invalid.
        dir = input('')
    if dir == 'F' or dir == 'f':      
        print('''You just entered the dark, scary house!
        It feels a bit dry and cold, with a slightly chilly breeaze.
        You are currently at the door way, and in front of you is a pitch black hallway.
        Move forward.''')
        dir = input('')               #Prompts the user to move forward a few steps to get to new destination.
        while dir != 'F' and dir != 'f':
            print('''There is an obstraction in that direction.
            You are advised to change directions.''')
            dir = input('')           #Prompts the user to enter valid input.
        if dir == 'F' or dir == 'f':
            print('''You took four steps forward, now you are at a crossroads.
            You either go forward down the the unsettling hallway.
            Or you either turn left facing another spin chilling hallway
            You choice.''')
            dir = input('Enter F to move forward or L to face left: ')
                                        #Prompts the user to either move left or forward
            while dir != 'F' and dir != 'f' and dir != 'L' and dir != 'l':
                print('''There is an obstraction in that direction.
                You are advised to change directions.''')
                dir = input('')
            if dir == 'F' or dir == 'f':
                print('''You took five steps down the hallway and the it seems to be turning left.
                But wait, you see an entity materializing.
                It's a ghost! It seems like it wants to communicate with you, listen.
                GHOST: "The path you are on may or may not lead to your destination."
                The ghost then suddenly disappears without any further explaination.
                You have no choice but to move forward. Proceed facing that direction by entering L ''')
                dir = input('')          #Prompts user to face left
                while dir != 'L' and dir != 'l':
                    print('Face left!')  #Prompts user to face left, if input is invalid
                    dir = input('')
                if dir == 'L' or dir == 'l':
                                         #If the user's entry is valid, code will run.
                    print('Now move forward.')
                    dir = input('')      
                    while dir != 'F' and dir != 'f':
                        print('Move forward')
                                         #Prompts user to move forward after turnig left.
                        dir = input('')
                    if dir == 'F' or dir == 'f':
                        print('''You took four steps.
                        Now you have three choices to choose from.
                        You either go straight into the unholy.
                        You either go left into the abiss.
                        Or you either go right to meet your dismiss.
                        Make your choice!''')
                        dir = input('')   #Prompts the user to move forward, left or right.
                        while dir != 'F' and dir != 'f' and dir != 'L' and dir != 'l' and dir != 'R' and dir != 'r':
                            print('''There is an obstraction in that direction.
                            You are advised to change directions.''')
                        if dir == 'F' or dir == 'f':
                            print('''You moved four steps forward.
                            The wall in front of you is surprisingly pleasant for a haunted house.
                            You must be getting close...
                            Or not...
                            But either way, you can only move right.
                            Proceed on.''')
                            dir = input('') #
                            while dir != 'R' and dir != 'r':
                                print('''There is an obstraction in that direction.
                                You are advised to change directions.''')
                                dir = input('')
                            if dir == 'R' or dir == 'r':
                                print('''You took three steps forward.
                                You could continue forward as you are.
                                Or you could go left, to your new destination.
                                Your choice.''')
                                dir = input('')
                                while dir != 'F' and dir != 'f' and dir != 'L' and dir != 'l':
                                    print('''There is an obstraction in that direction.
                                You are advised to change directions.''')
                                    dir = input('')
                                while True:
                                    if dir == 'F' or dir == 'f':
                                        print('You took two steps')
                                        x = input('...')
                                        print('''And indeed your end is here.
                                        Game Over!''')
                                        break
                                    elif dir == 'L' or dir == 'l':
                                        print('''You took three steps left.
                                        But wait. The seems to be a flicker of light to your right.
                                        Care to investigate?''')
                                        dir = input('')
                                        while dir != 'R' and dir != 'r':
                                            print('''There is an obstraction in that direction.
                                            You are advised to change directions.''')
                                            dir = input('')
                                        if dir == 'R' or dir == 'r':
                                            print('You took two steps towards the light.')
                                            x = input('...')
                                            print('Congradualtion! You have escaped the dreadful Haunted house!')
                                            break
                        elif dir == 'L' or dir == 'l':
                            print('''You took five steps left.
                            There is two ways you could go.
                            You could either go straight.
                            Or you could either go right.''')
                            dir = input('')
                            while dir != 'F' and dir != 'f' and dir != 'R' and dir != 'r':
                                print('''There is an obstraction in that direction.
                                You are advised to change directions.''')
                                dir = input('')
                            if dir == 'F' or dir == 'f':
                                print('''You took three steps forward.
                                I hope you made the right choice.
                                You have a huge wall in front of you, 
                                and the room turns right.
                                Proceed.''')
                                dir = input('')
                                while dir != 'R' and dir != 'r':
                                    print('''There is an obstraction in that direction.
                                You are advised to change directions.''')
                                dir = input('')

                                if dir == 'R' or dir == 'r':
                                    print('''Wait, before going forward, the seems to be a ghost materializing
                                    in front of you.
                                    With a cold, dead stare the ghost is try to speak.
                                    Listen to it's cold, chilling words.''')
                                    x = input('...')
                                    print('''Ghost: 'Move forward and claim your prize. 
                                    I have been in this walls for centuries, I know whats best'.
                                    This ghost seems untrustworthy, so we are going to give you a chance to reverse
                                    back down the hall and back to your previous spot, just enter B.
                                    Or you could continue moving forward, your choice.
                                    But know that once you choose to go back, you will be forbidden to go reverse back.''')
                                    dir = input('')
                                    while dir != 'B' and dir != 'b' and dir != 'F' and dir != 'f':
                                        print('''There is an obstraction in that direction.
                                        You are advised to change directions.''')
                                        dir = input('')
                                    if dir == 'B' or dir == 'b':
                                        print('''You have moved three steps back.
                                        Your actions have led you to accept the left path as your destination.
                                        Proceed left.''')
                                        dir = input('')
                                        while dir != 'L' and dir != 'l':
                                            print('''There is an obstraction in that direction.
                                            You are advised to change directions.''')
                                            dir = input('')
                                        if dir == 'L' or dir == 'l':
                                            print('''You took six steps right.
                                            Is that...is that a ghost that is materializing in front of your eyes?
                                            Two ghost appearances in one night, this is really a haunted house!
                                            Let's hear it's bone chilling words.''')
                                            x = input('')
                                            print('''Ghost: The most fruitful paths are the most unexpected paths.
                                            Your path leads you right, again.''')
                                            dir = input('')
                                            while dir != 'R' and dir != 'r':
                                                print('''There is an obstraction in that direction.
                                                You are advised to change directions.''')
                                                dir = input('')
                                            if dir == 'R' or dir == 'r':
                                                print('''You took six steps right.
                                                Your choosen path leads you left.
                                                It seems that the end is near...''') 
                                                x = input('')
                                                print('''or is it!?
                                                Take a left turn.''')
                                                while dir != 'L' and dir != 'l':
                                                    print('''There is an obstraction in that direction.
                                                    You are advised to change directions.''')
                                                    dir = input('')
                                                while True:
                                                    if dir == 'L' or dir == 'l':
                                                        print('''It seems that you met your end.
                                                        Game Over.''')
                                                        break
                                    elif dir == 'F' or dir == 'f':
                                        print('''You took four steps before you felt this overwhelming feeling.
                                        Is it a feeling of disappointment
                                        Or is it a feeling of voictory?
                                        Keep moving to find out.''')
                                        dir = input('')
                                        while dir != 'f' and dir != 'f':
                                            print('''There is an obstraction in that direction.
                                                    You are advised to change directions.''')
                                            dir = input('')
                                        while True:
                                            if dir == 'F' or dir == 'f':
                                                print('You took four steps forward.')
                                                x = input('')
                                                print('''You reached a road block.
                                                Game Over.''')
                                                break
                            elif dir == 'R' or dir == 'r':
                                print('''You took six steps right.
                                The path you choosen leads you right again.
                                Proceed that direction.''')  
                                dir = input('')
                                while dir != 'R' and dir != 'r':
                                    print('''There is an obstraction in that direction.
                                        You are advised to change directions.''')
                                    dir = input('')
                                if dir == 'R' or dir == 'r':
                                    print('''You took half a dozen steps to the right.
                                    You came across a brick wall, your path leads you left.
                                    The energy in this part of the maze feels different.
                                    Proceed onward to discover the cause of this strange phenomenon.''')
                                    dir = input('')
                                    while dir != 'L' and dir != 'l':
                                        print('''There is an obstraction in that direction.
                                            You are advised to change directions.''')
                                        dir = input('')
                                    while True:
                                        if dir == 'L' or dir == 'l':
                                            print('''You took three steps to the left.
                                            The enegry feels a bit weird...''')
                                            x = input('')
                                            print('''It is because you have reached a road block in your path
                                            and can't travel any further.
                                            Game Over.''')
                        elif dir == 'R' or dir == 'r':
                            print('''You took three steps right.
                            You path leads you left.
                            Take your path.''')
                            dir = input('')
                            while dir != 'L' and dir != 'l':
                                print('''There is an obstraction in that direction.
                                        You are advised to change directions.''')
                                dir = input('')
                            if dir == 'L' or dir == 'l':
                                print('''You took four steps left.
                                Your path takes you forward
                                And it also takes you right.
                                Which direction seems pleasing to you?
                                Choose your path.''')
                                dir = input('')
                                while dir != 'L' and dir != 'l' and dir != 'R' and dir != 'r':
                                    print('''There is an obstraction in that direction.
                                        You are advised to change directions.''')
                                    dir = input('')
                                if dir == 'F' or dir == 'f':
                                    print('''You took three steps forward.
                                    On your right, theres a glimmer of light.
                                    Is it a crack in a door
                                    Or is it just an illusion?''')
                                    dir = input('')
                                    while dir != 'R' and dir != 'r':
                                        print('''There is an obstraction in that direction.
                                                You are advised to change directions.''')
                                    while True:
                                        if dir == 'R' or dir == 'r':
                                            print('You took two steps.')
                                            x = input('')
                                            print('''It's indeed a door!
                                            Well done, you won the maze.''')
                                            break
                                elif dir == 'R' or dir == 'r':
                                    print('You faced right. Move forward.')
                                    dir = input('')
                                    while dir != 'F' and dir != 'f':
                                        print('''There is an obstraction in that direction.
                                            You are advised to change directions.''')
                                    while True:
                                        if dir == 'F' or dir == 'f':
                                            print('You took two steps right.')
                                            x = input('')
                                            print('''You hit a road block.
                                            Seems that the maze was too much for you.
                                            Game Over.''')
                                            break
            elif dir == 'L' or dir == 'l':
                print('''You took four steps to the left before stubling across
                a three way path.
                You either go Forward, Right, or Left.
                Choose wisely.''')
                dir = input('')
                while dir != 'F' and dir != 'f' and dir != 'R' and dir != 'r' and dir != 'L' and dir != 'l':
                    print('''There is an obstraction in that direction.
                        You are advised to change directions.''')
                    dir = input('')
                if dir == 'F' or dir == 'f':
                    print('You took half a dozen steps forward before feeling a chilly breeze...')
                    x = input('')
                    print('''It's a ghost materializing!
                    It demands that you listen to its unholy words.
                    Ghost:'...'
                    *The ghost disapears without saying a single word.*
                    Uhm...''')
                    print('''ghosts are unpredictable.
                    Nonetheless, your path leads you right.
                    Proceed on.''')
                    dir = input('')
                    while dir != 'R' and dir != 'r':
                        print('''There is an obstraction in that direction.
                            You are advised to change directions.''') 
                        dir = input('')
                    if dir == 'R' or dir == 'r':
                        print('''You took another half a dozen steps, this time to the right.
                        Your path leads you left.
                        It's appropriate to note that the energy on this side of the maze feels a bit heavy.
                        Maybe something is about to happen.
                        Proceed on.''')
                        dir = input('')
                        while dir != 'L' and dir != 'l':
                            print('''There is an obstraction in that direction.
                                You are advised to change directions.''')
                            dir = input('')
                        while True:
                            if dir == 'L' or dir == 'l':
                                print('You took three steps to the left...')
                                x = input('')
                                print('''Unfortunately the road ends here.
                                The maze wins this one.
                                Game Over.''')
                                break

                elif dir == 'R' or dir == 'r':
                    print('''You took five steps to the right.
                    The path suddenly splits into two directions.
                    You either move forward and continue your path.
                    Or go left and start a new journey.
                    Your choice.''')
                    dir = input('')
                    while dir != 'F' and dir != 'f' and dir != 'L' and dir != 'l':
                        print('''There is an obstraction in that direction.
                            You are advised to change directions.''')
                        dir = input('')
                    if dir == 'L' or dir == 'l':
                        print('''You took four steps to the left before your path you right.
                        There is a refreshing feeling about this part of the maze, maybe good news lies ahead.
                        Or maybe new challenges are ahead.
                        Proceed right.''')
                        dir = input('')
                        while dir != 'R' and dir != 'r':
                            print('''There is an obstraction in that direction.
                                You are advised to change directions.''')
                            dir = input('')
                        if dir == 'R' or dir == 'r':
                            print('''You took three steps right before the path chosen led you to a road
                            with two paths.
                            You either move forward or take a left.
                            One of this paths is the source of the refreshing feeling you felt earlier.
                            Choice wisely.''')
                            dir = input('')
                            while dir != 'F' and dir != 'f' and dir != 'L' and dir != 'l':
                                print('''There is an obstraction in that direction.
                                    You are advised to change directions.''')
                                dir = input('')
                            while True:
                                if dir == 'F' or dir == 'f':
                                    print('You took two steps forward...')
                                    x = input('')
                                    print('''You have ran out of luck, by runnig into a brick wall.
                                    Game Over.''')
                                    break

                                elif dir == 'L' or dir == 'l':
                                    print(''''You took three steps to the left before your path
                                    lead you right.
                                    Proceed on.''')
                                    dir = input('')
                                    while dir != 'R' or dir != 'r':
                                        print('''There is an obstraction in that direction.
                                            You are advised to change directions.''')
                                        dir = input('')
                                    while True:
                                        if dir == 'R' or dir == 'r':
                                            print('''You took two steps right.
                                            And you have found the end of the maze.
                                            Congradulations for beating the maze.''')
                                            break

                    elif dir == 'F' or dir == 'f':
                        print('''You took three steps forward.
                        Your path leads you left.
                        Proceed on.''')
                        dir = input('')
                        while dir != 'L' and dir != 'l':
                            print('''There is an obstraction in that direction.
                                You are advised to change directions.''')
                            dir = input('')
                        if dir == 'L' or dir == 'l':
                            print('''You took four steps to the left.
                            Now there is two paths you have to choose from.
                            You either choose to go forward or right.
                            Your choice.''')
                            dir = input('')
                            while dir != 'F' and dir != 'f' and dir != 'R' and dir != 'r':
                                print('''There is an obstraction in that direction.
                                    You are advised to change directions.''')
                                dir = input('')
                            while True:     
                                if dir == 'F' or dir == 'f':
                                    print('''You took three steps forward according to your chosen path.
                                    On your right there is a weirdly shaped wall.
                                    Investigate further.''')
                                    dir = input('')
                                    while dir != 'R' and dir != 'r':
                                        print('''There is an obstraction in that direction.
                                        You are advised to change directions.''')
                                        dir = input('')
                                    while True:
                                        if dir == 'R' or dir == 'r':
                                            print('You took two steps to the right.')
                                            x = input('')
                                            print('''It turns out that the weirdly shaped wall is actually a door that leads outside the maze.
                                            Congradualation!''')
                                            break                                       
                                elif dir == 'R' or dir == 'r':
                                    print('''You took two steps to the right.
                                    But unfortunately it is not the right path.
                                    Game over.''')
                                    break            
                elif dir == 'L' or dir == 'l':
                    print('''You took five steps to the left.
                    Now you are faced with two choices, you either go right or forward.
                    Choose wisely.''')
                    dir = input('')
                    while dir != 'F' and dir != 'f' and dir != 'R' and dir != 'r':
                        print('''There is an obstraction in that direction.
                            You are advised to change directions.''')
                        dir = input('')
                    if dir == 'F' or dir == 'f':
                        print('''You took three steps forward.
                        On your right lies a long, dark cold hall that seem to be going forever
                        but may perphaps lead to victory.
                        Proceed on.''')
                        dir = input('')
                        while dir != 'F' and dir != 'f':
                            print('''There is an obstraction in that direction.
                                You are advised to change directions.''')
                            dir = input('')
                        while True:
                            if dir == 'F' or dir == 'f':
                                print('''After terribly long walk through the hall, you have reached the end.
                                With much disappointment, you are met with nothing but gray wall.
                                Game Over.''')
                                break
                    elif dir == 'R' or dir == 'r':
                        print('''After half a dozen steps, you reach the point of your path where it turns right.
                        Proceed on.''')
                        dir = input('')
                        while dir != 'R' and dir != 'r':
                            print('''There is an obstraction in that direction.
                                You are advised to change directions.''')
                            dir = input('')

                        if dir == 'R' or dir == 'r':
                            print('''You took another half a dozen steps before reaching the end of the hall.
                            From here the hall only turns left.
                            This direction seems special.
                            Find out why.''')
                            dir = input('')
                            while dir != 'L' and dir != 'l':
                                print('''There is an obstraction in that direction.
                                    You are advised to change directions.''')
                                dir = input('')
                            while True:
                                if dir == 'L' or dir == 'l':
                                    print('You took two steps left.')
                                    x = input('')
                                    print('''Unfortunately, it's not the good kind of special.
                                    Game Over.''')
                                    break

elif sce == 'B' or sce == 'b':
    print('''Welcome to the Jungle Maze
    To move forward enter F, to move left enter L, to move right enter R.
    Once you made your choice there is no going back!
    It is forbidden for you to travel the same path twice!''')
    dir = input('Enter F to enter the Jungle: ')
    while dir != 'F' and dir != 'f':
        print('''There is an obstraction in that direction.
            You are advised to change directions.''')
        dir = input('')
    if dir == 'F' or dir == 'f':
        print('''You are at the start of the Jungle.
        You get welcomed by all sorts of rackets from the Jungle.
        It takes you a minute before you are able to clear your head and focus.
        Move forward.''')
        dir = input('')
        while dir != 'F' and dir != 'f':
            print('''There is an obstraction in that direction.
                You are advised to change directions.''')
            dir = input('')
        if dir == 'F' or dir == 'f':
            print('''You took four steps forward.
            You can't move any further because there are dense trees in front of you.
            You could either go left or go right.
            Your choice.''')
            dir = input('')
            while dir != 'R' and dir != 'r' and dir != 'L' and dir != 'l':
                print('''There is an obstraction in that direction.
                    You are advised to change directions.''')
                dir = input('')
            if dir == 'L' or dir == 'l':
                print('''You took five steps to the left.
                You can't go any further because of the dense Jungle.
                Over the Jungle clatter, you suddenly hear a distinct sound.
                You are bewildered by the sound, wondering what kind of animal could that be.
                You have two choices to make.
                You either go Left.
                Or you either go right.
                Its your choice to make.''')
                dir = input('')
                while dir != 'R' and dir != 'r' and dir != 'L' and dir != 'l':
                    print('''There is an obstraction in that direction.
                        You are advised to change directions.''')
                    dir = input('')
                if dir == 'R' or dir == 'r':
                    print('''You took three steps to the right before you hear that bone chilling sound again.
                    But this much it's much closer.
                    You get pulled out of your trance by a deep, stern voice.
                    Mysterious Voice: Travller! Do not weary or else this Jungle will eat you alive.
                    The mysterious and sound stops and everything goes back to normal.
                    The only path you can take is left.
                    Proceed on.''')
                    dir = input('')
                    while dir != 'L' and dir != 'l':
                        print('''There is an obstraction in that direction.
                            You are advised to change directions.''')
                        dir = input('')
                    while True:    
                        if dir == 'L' or dir == 'l':
                            print('''You took half a dozen steps to the left.
                            But the path ahead is covered with dense trees and bushes.
                            You are trapped!
                            Game Over.''')
                            break
                
                elif dir == 'L' or dir == 'l':
                    print('''You took three steps to the left.
                    All of a sudden there is a slight but noticeable breeze.
                    You can't help but feel like you are being watched.
                    It's hard to dimiss the feeling after hearing that unsettling sound earlier.
                    But there's no time to waste.
                    Your path leads you right.
                    Proceed on.''')
                    dir = input('')
                    while dir != 'R' and dir != 'r':
                        print('''There is an obstraction in that direction.
                            You are advised to change directions.''')
                        dir = input('')
                    while True:
                        if dir == 'R' or dir == 'r':
                            print('You took half a dozen steps to the right.')
                            x = input('')
                            print('''But the jungle is to dense for you to move forward.
                            Game Over.''')
                            break

            elif dir == 'F' or dir == 'f':
                print('''You took two steps to the right.
                Before moving on, you have a decision to make.
                You either go forward, which seems like a short path.
                Or you either go left.
                Your choice.''')
                dir = input('')
                while dir != 'F' and dir != 'f' and dir != 'l' and dir != 'L':
                    print('''There is an obstraction in that direction.
                        You are advised to change directions.''')
                    dir = input('')
                if dir == 'L' or dir == 'l':
                    print('''You took half a dozen steps to the left.
                    The Jungle seems to open up abit the further you move.
                    The only clear path is left.
                    Proceed on.''')
                    dir = input('')
                    while dir != 'L' and dir != 'l':
                        print('''There is an obstraction in that direction.
                            You are advised to change directions.''')
                        dir = input('')
                    if dir == 'L' and dir == 'l':
                        print('''You took nine steps to the left.
                        In the brush in front of you, you notice a unique monkey.
                        It's an unusual looking monkey, maybe never discovered yet.
                        But it disappears as quick as it strikes curiosity in an unsuspecting travels.
                        Okay, you have a maze to finish.
                        The clearest path is on you right.
                        Proceed on!''')
                        dir = input('')
                        while dir != 'R' and dir != 'r':
                            print('''There is an obstraction in that direction.
                                You are advised to change directions.''')
                            dir = input('')
                        if dir == 'R' or dir == 'r':
                            print('''You took three steps to the right.
                            You landed on a path that is perpendicular to your previous path.
                            You either go left.
                            Or you either go right.
                            You choice.''')
                            dir = input('')
                            while dir != 'R' and dir != 'r' and dir != 'L' and dir != 'l':
                                print('''There is an obstraction in that direction.
                                    You are advised to change directions.''')
                                dir = input('')
                            while True:
                                if dir == 'R' or dir == 'r':
                                    print('You took ten steps to the right.')
                                    x = input('')
                                    print('''Unfortunately the path you chose is dense.
                                    Game Over.''')
                                    break
                                elif dir == 'L' or dir == 'l':
                                    print('''Congradulation!
                                    You found an opening and escaped through it.
                                    Good Game.''')
                                    break
                
                while True:
                    if dir == 'F' or dir == 'l':
                        print('''You took the wrong path, you should have gone the other way.
                        Game over.''')
                        break

elif sce == 'C' or sce == 'c':
    print('''Welcome to the Medieval Maze
    To move forward enter F, to move left enter L, to move right enter R.
    Once you made your choice there is no going back!
    It is forbidden for you to travel the same path twice!''')
    dir = input('Enter F to enter the Castle: ')
    while dir != 'F' and dir != 'f':
        print('''There is an obstraction in that direction.
            You are advised to change directions.''')
        dir = input('')
    if dir == 'F' or dir == 'f':
        print('''You are at the start of the Castle.
        It seems to be dusty and full of rusty metals, its a mess.
        Enter F to go forward.''')
        dir = input('')
        while dir != 'F' and dir != 'f':
            print('''There is an obstraction in that direction.
                You are advised to change directions.''')
            dir = input('')

        if dir == 'F' or dir == 'f':
            print('''You took four steps forward.
            Amids all the dust created by your foot steps, there seems to be another path on your right.
            You either go straight.
            Or you either go right.
            Make your choice.''')
            dir = input('')
            while dir != 'F' and dir != 'f' and dir != 'R' and dir != 'r':
                print('''There is an obstraction in that direction.
                    You are advised to change directions.''')
                dir = input('')
            if dir == 'F' or dir == 'f':
                print('''You took five steps forward.
                Would you look at that, there is another path on your right.
                You either choose to continue your path.
                Or you either give in and turn right.
                Your choice.''')
                dir = input('')
                while dir != 'F' and dir != 'f' and dir != 'R' and dir != 'r':
                    print('''There is an obstraction in that direction.
                        You are advised to change directions.''')
                    dir = input('')
                if dir == 'R' or dir == 'r':
                    print('''You took five steps to the right.
                    Now! You either go forward and continue you journey.
                    Or you can turn right and change paths.
                    It's important to note that one of the paths doesn't feel right to you.
                    Your choice which one it is.''')
                    dir = input('')
                    while dir != 'F' and dir != 'f' and dir != 'R' and dir != 'r':
                        print('''There is an obstraction in that direction.
                            You are advised to change directions.''')
                        dir = input('')
                    if dir == 'F' or dir == 'f':
                        print('''You took two steps forward.
                        Left is the only accessible path, but there seems to be a green object blocking the path''')
                        x = input('...')
                        print('''The green object starts moving a bi!
                        Now you can take a good look at it.
                        Wait! You realize that it's a Gablin!
                        You are astonished!
                        You can choose to move passed it, without disturbing it.
                        Or you can simply disrupt it's peace by typing "Hey Ugly".
                        I don't recommend that.
                        But it's completely up to you.''') 
                        dir = input('')
                        while dir != 'F' and dir != 'f' and dir != 'Hey Ugly' and dir != 'hey ugly' and dir != 'Hey ugly':
                            print('''Invalid input.
                                You are advised to enter a valid input.''')
                            dir = input('')
                        while True:
                            if dir == 'F' or dir == 'f':
                                print('''You took five steps forward.
                                Choosing to leave the Goblin at peace.''')
                                x = input('...')
                                print('''Congradulations...
                                You have completed the Medieval Times Maze.''')
                                break
                            elif dir == 'Hey Ugly' and dir == 'Hey ugly' and dir == 'hey ugly':
                                print('''The Goblin jumps up with vicious velocity and anger in it's eyes.
                                It attacks you, leaving you paralysed and on the verge of death.
                                Who knew such a small creature can be capable of such potent aggression.
                                Game Over.''')
                                break
                    elif dir == 'R' or dir == 'r':
                        print('''You took five steps to the right.
                        In front of you is a large portrait honouring all the fallen knights, who fought for this very castle.
                        What a sight to behold!
                        Your path leads you left.
                        Proceed on!''')
                        dir = input('')
                        while dir != 'l' and dir != 'L':
                            print('''There is an obstraction in that direction.
                                You are advised to change directions.''')
                            dir = input('')
                        if dir == 'L' or dir == 'l':
                            print('''You took another five steps but this time to the left.
                            There seems to be a cool breeze flowing through this part of the castle.
                            It might be an indication that the exit door is near.
                            Or it might be just a broken window.
                            You have two paths i front of you.
                            You either move forward.
                            Or you go left.
                            Your choice''')
                            dir = input('')
                            while dir != 'F' and dir != 'f' and dir != 'L' and dir != 'l':
                                print('''There is an obstraction in that direction.
                                    You are advised to change directions.''')
                                dir = input('')
                            if dir == 'L' or dir == 'l':
                                print('''You took eight steps to the left.
                                The breezed seemed to be getting chiller as you made your way down that path.
                                Your path continuous straight.
                                But there's also a path on your right that you can take.
                                Choose your fate.''')
                                dir = input('')
                                while dir != 'F' and dir != 'f' and dir != 'L' and dir != 'l':
                                    print('''There is an obstraction in that direction.
                                        You are advised to change directions.''')
                                    dir = input('')
                                if dir == 'L' or dir == 'l':
                                    print('''You took three steps to the right.
                                    The breeze that you have been feeling seems to be getting more noticeable.
                                    Your path leads you right.
                                    Proceed on.''')  
                                    dir = input('')
                                    while dir != 'R' and dir != 'r':
                                        print('''There is an obstraction in that direction.
                                            You are advised to change directions.''')
                                        dir = input('')
                                    while True:
                                        if dir == 'R' or dir == 'r':
                                            print('You took three steps to the right.')
                                            x = input('...')
                                            print('''You seem to have reached the end of the maze.
                                            Congradulations!
                                            You did reach the end of the maze!''')
                                            break

                                while True:
                                    if dir == 'F' or dir == 'f':
                                        print('''You took two steps forward.
                                        Unfortunalety by you second step you accidentally stepped on a trapped door.
                                        You fell down an almost endless hole down to the bottom.
                                        Game Over.''') 
                                        break       

                            while True:
                                if dir == 'F' or dir == 'f':
                                    print('''You took three steps forward.
                                    But unfortunately it's the end of the path.
                                    Game Over.''')
                                    break

                        
                while True:
                    if dir == 'F' or dir == 'f':
                        print('You took five steps forward.')
                        x = input('')
                        print('''You had two chances to change your fate.
                        You didn't take neither.
                        You mistakes led you into an abiss of traps.
                        Game Over.''')
                        break


            elif dir == 'R' or dir == 'r':
                print('''You took four steps to the right.
                Before moving any further, there is a different path on your right.
                You either move forward.
                Or you can turn to a new direction.
                Your choice.''')
                dir = input('')
                while dir != 'F' and dir != 'f' and dir != 'R' and dir != 'r':
                    print('''There is an obstraction in that direction.
                        You are advised to change directions.''')
                    dir = input('')
                if dir == 'F' or dir == 'f':
                    print(''''You took half a dozen steps forward.
                    There is surprisingly a cool breeze flowing through this side of the palace.
                    Maybe you are getting closer
                    Maybe not.
                    But either way, there are two paths in front of you.
                    You either go forward.
                    Or you go left.
                    Your choice.''')
                    dir = input('')
                    while dir != 'F' and dir != 'f' and dir != 'L' and dir != 'l':
                        print('''There is an obstraction in that direction.
                            You are advised to change directions.''')
                        dir = input('')
                    if dir == 'L' or dir == 'l':
                        print('''You took eight steps to the left.
                        The slight breeze is becoming more noticeable.
                        And there are two paths in front of you.
                        One goes left.
                        The other one goes forward.
                        The breeze is flowing from one of the paths.
                        Make your choice.''')
                        dir = input('')
                        while dir != 'F' and dir != 'f' and dir != 'L' and dir != 'l':
                            print('''There is an obstraction in that direction.
                                You are advised to change directions.''')
                            dir = input('')
                        if dir == 'L' or dir == 'l':
                            print('''You took three steps to the left.
                            Your path leads you right.
                            And it's important to note that you are still feeling the breeze,
                            meaning you made the right choice.
                            Proceed on.''')
                            dir = input('')
                            while dir != 'R' and dir != 'r':
                                print('''There is an obstraction in that direction.
                                    You are advised to change directions.''')
                                dir = input('')
                            while True:
                                if dir == 'R' or dir == 'r':
                                    print('You took two steps to the right.')
                                    x = input('...')
                                    print('''Congradulation!
                                    You've reached the end of the maze.''')
                                    break
                        while True:
                            if dir == 'F' or dir == 'f':
                                print('''You took two steps forward.
                                Unfortunately, on your third step you accidentally stepped on a trapped door.
                                You fell down an endless hole.
                                Game Over''')
                                break

                    while True:
                        if dir == 'F' or dir == 'f':
                            print('''You took two steps forward.
                            Unfortunately, on your third step you accidentally stepped on a trapped door.
                            You fell down an endless hole.
                            Game Over''')
                            break
                       
                

                while True:
                    if dir == 'R' or dir == 'r':
                        print('''You took two steps forward.
                        Unfortunately, on your third step you accidentally stepped on a trapped door.
                        You fell down an endless hole.
                        Game Over''')
                        break       
    
            



    
