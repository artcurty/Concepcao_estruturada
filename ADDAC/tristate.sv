module tristate(input logic [0:0] a, input logic en, output tri [0:0] y);
assign y = en ? a : 1'bz;
endmodule 