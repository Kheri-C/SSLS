function [angPred,motors] = predictang(powL,powR,powF,powB,ratioThres,powThres)
    %if powL > powThres || powR > powThres || powF > powThres ||  powB > powThres
        % Save the biggest and smallest value between L and R
        if powL >= powR
            maxLR = powL;
            minLR = powR;
        else
            maxLR = powR;
            minLR = powL;
        end
        % Save the biggest and smallest value between F and B
        if powF >= powB
            maxFB = powF;
            minFB = powB;
        else
            maxFB = powB;
            minFb = powF;
        end
        % Divide the min by the max to obtain the ratio
        ratioLR = minLR/maxLR;
        ratioFB = minFB/maxFB;
        % Decide where the sound comes from
        if ratioLR >= ratioThres
            if ratioFB >= ratioThres
                disp("The sound comes from above or below")
                angPred = NaN;
                motors = 0x04; % Up code
            else
                if powF > powB
                    disp("The sound comes from the front")
                    angPred = 0;
                    motors = 0x02;
                else
                    disp("The sound comes from the back")
                    angPred = 180;
                    motors = 0x03;
                end
            end
        else
            if ratioFB >= ratioThres
                if powL > powR
                    disp("The sound comes from the left")
                    angPred = 90;
                    motors = 0x00;
                else
                    disp("The sound comes from the right")
                    angPred = 270;
                    motors = 0x01;
                end
            else
                if powL > powR
                    if powF > powB
                        disp("The sound comes from the front left")
                        angPred = 45;
                        motors = 0x06;
                    else
                        disp("The sound comes from the back left")
                        angPred = 135;
                        motors = 0x07;
                    end
                else
                    if powF > powB
                        disp("The sound comes from the front right")
                        angPred = 315;
                        motors = 0x0A;
                    else
                        disp("The sound comes from the back right")
                        angPred = 225;
                        motors = 0x0B;
                    end
                end
            end
        end
    %else
        %disp("The system did not receive enough power")
    %end
end