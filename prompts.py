
start_prompt = "make a poem using all the concepts from this list of concepts : Quantum computing,AI,Nanotechnology,Genetic engineering,Augmented reality,Blockchain,Robotics,Biotechnology,IoT,3D printing,Virtual reality,Renewable energy,Cybersecurity,Neurotechnology,Space exploration,Autonomous vehicles,Bioinformatics,Quantum cryptography,Wearable technology,Synthetic biology,Cloud computing,Holography,Machine learning,Gene therapy,Quantum sensors,5G networks,Neuromorphic engineering,Quantum simulation,Bionic implants,Quantum metrology. exmple converstation <user>: make a sentence using all o this concepts:art,music,ai,drawing. <answer> As the AI-generated music swirled through the air, the artist's imagination was sparked by the vibrant colors of the digital canvas unfolding before her eyes, and she began to draw inspiration from the sonic patterns, weaving together the melodic lines with bold brushstrokes that danced across the virtual easel, as if the very notes themselves were taking shape in a mesmerizing fusion of drawing, and music. "


feedback_prompt = f"""please do the folowing steps:1. check what where all of the concepts i have asked you to provide a poem about.  
step 2. check what concepts from the concepts you have been provided you forgot the include in the poem 
step:3 you should say what are the  missing concepts that the  asistant needs to add to the poem. here is an 
exmple: <user>: make a poem about the folowing subjects: football, waterball, tenis,soccer, and basketball  

<asistant>  The Pitch, the Court, the Field of Dreams
Where cleats meet turf, where balls are spun,
A symphony of sweat and fun.
Football, Soccer, Basketball too,
Three games unite, with passions anew.

In autumn's crisp, when leaves turn gold,
Football's tackle, strength to behold.
The quarterback's call, the running back's pace,
A dance of might, a test of space.

Winter's chill, when snowflakes fall,
Soccer's dribble, walls to enthrall.
The goalkeeper's leap, the striker's aim,
A battle of wills, with each player's claim.

Spring's awakening, when buds unfold,
Basketball's swish, shots to be told.
The point guard's pass, the center's might,
A harmony of pace, a dance in flight.

Summer's warmth, when sunbeams shine,
These three games merge, in one divine line.
United we play, with hearts aglow,
For love of sport, and joy to show. 
<you> 
step 1: i have been asked to provide a poem about the folowing subjects:
1.basketball
2. soccer
3.football 
4. tennis
5.waterball
step 2: i forogot to include in the poem the folowing subjetcs:
1. tennis
2. water ball

step 3: you need to add the concepts of tenis and waterball to the peom


"""


refine_prompt = "make a batter new answer using the feedback you have gotten for exmple > intialText :"

