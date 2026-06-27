class Solution {
    public int carFleet(int target, int[] position, int[] speed) {
      

        int [][] couples = new int[position.length][];
        for(int i=0;i<position.length;i++) couples[i] = new int[]{position[i],speed[i]};
        Arrays.sort(couples,(a,b)->{return Integer.compare(a[0],b[0]);});
        //sorting by position, using lambda, sorts in O(nlogn)

        /*when cars intersect/collide, we only keep the one ahead, as it will
         become the new speed bottleneck, and we must evaluate from right to left*/


        ArrayDeque<int[]> stack = new ArrayDeque<>();
        for(int i = couples.length-1;i>-1;i--){//traversing in reverse order
        /*basically, we put in first element (starting from the end) if 
        there is a collision with next one, we don't add it, if there is none
        we add it as a new fleet/cluster and will be comparing to that one since it 
        is both behind in position and speed (at least before target)*/

        /*
        to compute collision, we do the same math as earlier,
        p1+t(s1)=p2+t(s2)  <=>
        t=(p2-p1)/(s2-s1)    ATTENTION! division by 0 is risky, however, our isCollision won't
        evaluate if they have equal speed, which is what causes division by 0 so we are straight

        now we plug collision time in the position equation to figure out collision position, if it is <= 
        target then we do not add the car if not we add it

        col = p1 + s1((p2-p1)/(s2-s1))
        */
        //if(stack.isEmpty()||((stack.peek()[1]<couples[i][1])&&(couples[i][0]+couples[i][1]*(stack.peek()[0]-couples[i][0])/(stack.peek()[1]-couples[i][1]))<=target)) stack.push(couples[i]);

        /*
        this collision computation is quite complex, we can simply solve for p + ts = target for both and see if the new one arrives before the one on top 
        of the stack (implying a collision)

        t =(target-p)/s assuming non-zero speed
        */
        if(stack.isEmpty()||(stack.peek()[1]!=0&&couples[i][1]!=0&&((double)(target-couples[i][0])/couples[i][1]>(double)(target-stack.peek()[0])/stack.peek()[1])))
            stack.push(couples[i]);

        else continue;
        }
        return stack.size();
    }   
}
//runs in O(n) space, O(nlogn) time








/*
        Here, to know if a car will form a fleet, it seems like we need to do
        a simple computation being will it hit a car in front of it 
        before hitting destination, the brute force approach would be to have a pointer going through
        each car and then lineraly check each car (ahead) to see if it will hit it before destination
        and if yes merge the two cars into one cluster starting at the hit point and going at the 
        slowest out of the two's speed, this would run in O(n^2) and seems sub-optimal to implement too
        we know that a car can only hit a car infront of it, hence if we had to use a monotonic stack here,
        it might be an increasing one, let's try to find an solution using an increasing monotonic stack.
        (increasing in terms of position)
        */

        /*if all cars are ordered increasingly in terms of positon, (which they are), we can still get colisions
        but it simply depends on the speed of both cars and their colision point if the frontCar is slower than the
        back car, hence shouldn't we set an array of position-speed couples, then sort them based on positon, and 
        then rather build an increasing monotonic stack based on speed where we do the computation whenever a car
        is slower then the car behind it (cluster risk) and then define the resulting cluster in the stack.
        */

        /* building the stack

        int [int[]] couples = new int[position.lenght];
        for(int i=0;i<position.length;i++) couples[i] = new int[]{position[i],speed[i]};
        /*here we now need to sort based on positon, since position is now coupled, to 
        speed, we will use the built-in sort O(nlogn) and use a lambda expression to specify
        sorting on the 0th index

        Arrays.sort(couples,(a,b)->{a[0].compareTo(b[0])});

        /* now that we have a position sorted position-speed couples, let's implement a monotonic
        increasing stack based on speed

        ArrayDeque<int[]> stack = new ArrayDeque<>();
        int clusters = 0;
        for(int i=0;i<couples.lenght;i++){
            if(stack.isEmpty()||stack.peek()[1]<=couples[i][1]) stack.push(couples[i]);
            else{
                while(!stack.isEmpty() && stack.peek()[1]>couples[i][1]){
                    /*
                    here two scenarios exist, either the front car and back car meet before the 
                    end line (+1 cluster), they merge as a new car that has position their meet point
                    (since this is a monotonic stack, the previous cars are colision safe and it is hence ok to do that),
                    or they meet past the end line, and hence never cluster into 1, and we hence do cluster++ on each car 
                    we clear from the stack to make it monotonic and make the stack monotonic again.
                    

                    /*let's find the computation for colision position
                    p1 + t(s1) = p2 + t(s2) <=>  t(s1-s2) = (p2-p1)/(s1-s2) (collition time)
                    collision position is collision time plugged into the front car (slowest)'s 
                    position eq so : 
                    
                    cp = p2 + s2((p2-p1)/(s1-s2))

                    let's now implement that
                    


                    int colisionPosition = couples[i][0] + coupes[i][1]*((couples[i][0]-stack.peek()[0])/(stack.peek()[1]-couples[i][1]));
                    
                    //scenario where we do have a colision
                    if(colisionPosition<=target){
                        /*now we need to watch out as we are changing the position of an element of the stack
                        the stack will remain monotonic in terms of speed, but it might not be anymore in terms of
                        position, can this break our solution or is it fine ? most likley not, then rather than 
                        pushing it right away into the stack, can't we simply not insert it back into the array at the right position ?
                        we are hitting a wall.
                    }

                }
            }
        }
        */
