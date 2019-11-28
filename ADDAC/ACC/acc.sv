module acc(a, clk, y);
input logic [0:0]a;	
input logic clk;	
output logic [0:0]y;
		always@(posedge clk) begin
		y <= a;
	end
endmodule