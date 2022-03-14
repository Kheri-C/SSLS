function [powL,powR,powF,powB] = rec(idL,idR,idF,idB,rectime)
    % Specify the recording time in seconds

    % Definition of the sampling frequency
    Fs = 44100;
    % Definition of the audio recorders
    micRrecorder = audiorecorder(Fs,16,1,idR);
    micLrecorder = audiorecorder(Fs,16,1,idL);
    micFrecorder = audiorecorder(Fs,16,1,idF);
    micBrecorder = audiorecorder(Fs,16,1,idB);
    % Start recording
    disp('Recording started');
    record(micRrecorder);
    record(micLrecorder);
    record(micFrecorder);
    record(micBrecorder);
    % Halt the execution so the recording lasts as indicated
    pause(rectime);
    % Stop recording
    stop(micRrecorder);
    stop(micLrecorder);
    stop(micFrecorder);
    stop(micBrecorder);
    disp('Recording ended');
    % Convert the audio into numberical data
    datamicR = getaudiodata(micRrecorder);
    datamicL = getaudiodata(micLrecorder);
    datamicF = getaudiodata(micFrecorder);
    datamicB = getaudiodata(micBrecorder);
    %Obtain the power of each signal
    powR = power(rms(datamicR),2);
    powL = power(rms(datamicL),2);
    powF = power(rms(datamicF),2);
    powB = power(rms(datamicB),2);
end