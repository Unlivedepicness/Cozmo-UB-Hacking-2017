import cozmo
import random


def constant_speech(jokes, speed):
    return [[(joke, speed)] for joke in jokes]


non_offensive_jokes = [
    [("knock knock", 0.7), ("race condition", 0.7), ("who's there", 0.7)]
]

chuck_norris_jokes = constant_speech([
    "When Chuck Norris throws exceptions, it's across the room.",
    "All arrays Chuck Norris declares are of infinite size, because Chuck Norris knows no bounds.",
    "Chuck Norris doesn't have disk latency because the hard drive knows to hurry the hell up, or else.",
    "Chuck Norris writes code that optimises itself.",
    "Chuck Norris can't test for equality because he has no equal.",
    "Chuck Norris doesn't need garbage collection because he doesn't call .Dispose(), he calls .DropKick().",
    "Chuck Norris's first program was kill -9.",
    "Chuck Norris burst the dot com bubble.",
    "All browsers support the hex definitions #chuck and #norris for the colours black and blue.",
    "MySpace isn't really your space, it's Chuck's (he just lets you use it).",
    "Chuck Norris can write infinitely recursive functions and have them return.",
    "Chuck Norris can solve the Towers of Hanoi in one move.",
    "The only design pattern Chuck Norris knows is the God Object Pattern.",
    "Chuck Norris finished World of Warcraft.",
    "Project managers never ask Chuck Norris for estimations.",
    "Chuck Norris doesn't use web standards as the web will conform to him.",
    "'It works on my machine' always holds true for Chuck Norris.",
    "Chuck Norris doesn't do Burn Down charts, he does Smack Down charts.",
    "Chuck Norris can delete the Recycling Bin.",
    "Chuck Norris's beard can type 140 words per minute.",
    "Chuck Norris can unit test entire applications with a single assertion, 'it works'.",
    "Chuck Norris doesn't bug hunt as that signifies a probability of failure, he goes bug killing.",
    "Chuck Norris's keyboard doesn't have a Ctrl key because nothing controls Chuck Norris.",
    "Chuck Norris can overflow your stack just by looking at it.",
    "To Chuck Norris, everything contains a vulnerability.",
    "Chuck Norris doesn't sudo, the shell just knows it's him and does what it's told.",
    "Chuck Norris doesn't need a debugger, he just stares at the code until it confesses.",
    "Chuck Norris can access private methods.",
    "Chuck Norris can instantiate an abstract class.",
    "Chuck Norris does not need to know about Class Factory Pattern. He can instantiate interfaces.",
    "The class object inherits from Chuck Norris.",
    "For Chuck Norris, NP-Hard = O(1).",
    "Chuck Norris knows the last digit of Pi.",
    "Chuck Norris's Internet connection is faster upstream than downstream because even data has more incentive to run from him than to him.",
    "Chuck Norris solved the Travelling Salesman problem in O(1) time: break salesman into N pieces; kick each piece to a different city.",
    "No statement can catch the ChuckNorrisException.",
    "Chuck Norris doesn't pair program.",
    "Chuck Norris can write multi-threaded applications with a single thread.",
    "Chuck Norris doesn't need to use AJAX because pages are too afraid to postback anyways.",
    "Chuck Norris doesn't use reflection, reflection asks politely for his help.",
    "There is no Esc key on Chuck Norris' keyboard, because no one escapes Chuck Norris.",
    "Chuck Norris can binary search unsorted data.",
    "Chuck Norris doesn't needs try-catch, exceptions are too afraid to raise.",
    "Chuck Norris went out of an infinite loop.",
    "If Chuck Norris writes code with bugs, the bugs fix themselves.",
    "Chuck Norris hosting is 101% uptime guaranteed.",
    "Chuck Norris's keyboard has the Any key.",
    "Chuck Norris can access the database from the UI.",
    "Chuck Norris's programs never exit, they are terminated.",
    "Chuck Norris insists on strongly-typed programming languages.",
    "The Chuck Norris protocol design method has no status, requests or responses, only commands.",
    "Chuck Norris's programs occupy 150% of CPU, even when they are not running.",
    "Chuck Norris can spawn threads that complete before they are started.",
    "Chuck Norris's programs do not accept input.",
    "Chuck Norris can install iTunes without installing Quicktime.",
    "Chuck Norris doesn't need an OS.",
    "Chuck Norris's OSI network model has only one layer - Physical.",
    "Chuck Norris can compile syntax errors.",
    "Every SQL statement that Chuck Norris codes has an implicit 'COMMIT' in its end.",
    "Chuck Norris does not need to type-cast. The Chuck-Norris Compiler (CNC) sees through things. All the way down. Always.",
    "Chuck Norris does not code in cycles, he codes in strikes.",
    "Chuck Norris compresses his files by doing a flying round house kick to the hard drive.",
    "Chick Norris solved the halting problem.",
    "With Chuck Norris P = NP. There's no nondeterminism with Chuck Norris decisions.",
    "Chuck Norris can retrieve anything from /dev/null.",
    "No one has ever pair-programmed with Chuck Norris and lived to tell the tale.",
    "No one has ever spoken during review of Chuck Norris' code and lived to tell the tale.",
    "Chuck Norris doesn't use a GUI, he prefers COMMAND line.",
    "Chuck Norris doesn't use Oracle, he is the Oracle.",
    "Chuck Norris can dereference NULL.",
    "A diff between your code and Chuck Norris's is infinite.",
    "The Chuck Norris Eclipse plugin made alien contact.",
    "Chuck Norris is the ultimate mutex, all threads fear him.",
    "Don't worry about tests, Chuck Norris's test cases cover your code too.",
    "Each hair in Chuck Norris's beard contributes to make the world's largest DDOS.",
    "Chuck Norris's log statements are always at the FATAL level.",
    "Chuck Norris's database has only one table, 'Kick', which he drops frequently.",
    "Chuck Norris completed World of Warcraft.",
    "When Chuck Norris breaks the build, you can't fix it, because there is not a single line of code left.",
    "Chuck Norris types with one finger. He points it at the keyboard and the keyboard does the rest.",
    "Chuck Norris's programs can pass the Turing Test by staring at the interrogator.",
    "If you try to kill -9 Chuck Norris's programs, it backfires.",
    "Chuck Norris performs infinite loops in under 4 seconds.",
    "Chuck Norris can overwrite a locked variable.",
    "Chuck Norris knows the value of NULL, and he can sort by it too.",
    "Chuck Norris can install a 64-bit operating system on 32-bit machines.",
    "Chuck Norris can write to an output stream.",
    "Chuck Norris can read from an input stream.",
    "Chuck Norris never has to build his program to machine code. Machines have learnt to interpret Chuck Norris's code.",
    "Chuck Norris's unit tests don't run. They die.",
    "Chuck Norris causes the Blue Screen of Death.",
    "Chuck Norris can make a class that is both abstract and final.",
    "Chuck Norris could use anything in java.util.* to kill you, including the javadocs.",
    "Code runs faster when Chuck Norris watches it.",
    "Chuck Norris doesn't use REST, he waits.",
    "Everyone likes Chuck Norris on Facebook, whether they choose to or not.",
    "You can't follow Chuck Norris on Twitter, because he follows you.",
    "Chuck Norris's calculator has only 3 keys: 0, 1, and NAND.",
    "Chuck Norris only uses global variables. He has nothing to hide.",
    "Chuck Norris once implemented an HTTP server in a single printf call. It is now the heart of Apache webserver.",
    "Chuck Norris writes directly in binary. He then writes the source code as documentation for other programmers.",
    "Chuck Norris once shifted a bit so hard, it ended up on a different computer.",
    "Q: What is Chuck Norris's favorite Javascript framework? A: Knockout.js.",
], 1.1)

good_jokes = [
    [("yo mama so fat", 0.7), ("when I compute her mass with a recursive function", 0.7), ("i get a stack overflow", 1.5)],
    [("yo mama so fat", 0.7), ("she wears an asteroid belt", 0.7)],
    [("yo mama so fat", 0.7), ("obi wan saw her and said", 0.7), ("that's no moon", 1.5)],
    [("yo mama so fat", 0.7), ("schrodinger found her to be both inside and outside of the box", 1.0)],
    [("yo mama so fat", 0.7), ("she can collapse a wave function", 1.0), ("by sitting on it", 1.5)],
    [("yo mama so fat", 0.7), ("kurt godel used her to signify the set of all sets that contain themselves", 1.0)],
    [("yo mama so fat", 0.7), ("the probability that she is in an arbitrary point in a room", 0.9), ("is one", 1.5)],
    [("yo mama so fat", 0.7), ("she sat on a binary tree and flattened it to a linked list", 1), ("in constant time", 1.5)]
]

offensive_mode = False


def intent_jokes(robot: cozmo.robot.Robot):
    if offensive_mode:
        joke_pool = good_jokes
    else:
        joke_pool = chuck_norris_jokes + non_offensive_jokes

    joke = random.choice(joke_pool)
    for line in joke:
        robot.say_text(line[0], duration_scalar=line[1]).wait_for_completed()

    robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabExcited).wait_for_completed()


def intent_toggle_offensive_mode(robot: cozmo.robot.Robot):
    global offensive_mode

    offensive_mode = not offensive_mode

    if offensive_mode:
        robot.say_text('I will now tell offensive jokes').wait_for_completed()
    else:
        robot.say_text('I will now tell safe jokes').wait_for_completed()
