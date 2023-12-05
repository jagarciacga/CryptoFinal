%Isabel Robey, PEX2
%Collaborated with 2/c Church

%read contents of file into a string
textFile = fileread('ctf.txt');

%intialize variables for later use
matches = 0;
last_match = 0;
key_length = 0;

%for loop to iterate through shift values from 9 to 14 to estimate the key
for shift = 9:16
    a = textFile;
    %create a filler variable that creates a row vector of 1 with shift
    %specifying the length
    filler = zeros(1, shift);
    %combine filler with a to fill the blanks from the shift with zeros 
    b = [filler, a];
    %re-initialize for the loop throughs
    matches = 0;
    %for loop to iterate through the rows and find matches
    for i = 1:length(a)
        if a(i) == b(i)
            %if there is a match count it
            matches = matches + 1;
        end
    end

    %if matches is greater than last_match the key_length will be set to
    %whichever shift the program was on, telling us that that is the
    %current largest amount of matches
    if matches > last_match
        key_length = shift;
        %update last_match with the new maximum matches
        last_match = matches;  
    end
end

%display the key length
fprintf("key length: %d\n", key_length);

%create a new filler with value already set to key_length
filler1 = char(zeros(1, key_length));
%combine filler with textFile to fill the blanks from the shift with zeros
finalShift = [filler1, textFile];
    

%create the bins and sort
%start at 0, grab every nth letter depending on key_length
for shift_amount = 0:key_length-1

    %create file name that will change with amount/number of bin(s)
    fileName = ['output', num2str(shift_amount), '.txt'];
    %write to the file
    fileWrite = fopen(fileName, 'w');

    % Write the entire shifted_text to the text file
    %fprintf(fileWrite, '%s', shifted_text);

    %iterate through textFile, use mod to sort into bins
    for i = 1:length(finalShift)
        %find remainder of (i-1) divide by the key length and check if
        %equal
        %equal to the shift_amount
        if mod(i-1, key_length) == shift_amount
            %if so add the value to a file
            fprintf(fileWrite, '%c', finalShift(i));
        end
    end
    %close the file
    fclose(fileWrite);
    %display the file 
    disp([fileName]);
end

