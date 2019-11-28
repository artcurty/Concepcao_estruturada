module mux(input logic [0:0] d0, d1, input logic s, output tri [3:0] y);
 
 logic ns;
 inv inversor(s, ns);
 tristate t0(d0, ns, y);
 tristate t1(d1, s, y);
 
endmodule