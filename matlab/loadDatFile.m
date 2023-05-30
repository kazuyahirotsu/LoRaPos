function y = loadDatFile(filename)
fid = fopen(filename,'rb');
y = fread(fid, 'uint8=>double');
y = y-127.5;
y = y(1:2:end) + 1i*y(2:2:end);
end

