module addac(input logic [0:0]a, input logic sel0, sel1, input logic clk,
 output logic cout, output logic [0:0] s);
 
 logic [0:0] na;
 inv inversor(a, na);
 
 logic [0:0] mux0_out;
 mux mux0(a, na, sel0, mux0_out);
 
 logic [0:0] acc_out;
 logic [0:0] somador_out;
 
 somador somador(mux0_out, acc_out, sel0, somador_out, cout);
 
 mux mux1(mux0_out, somador_out, sel1, s); 
 
 endmodule 