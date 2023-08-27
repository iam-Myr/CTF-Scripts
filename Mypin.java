public void brute() {
        for (int i =0; i< 512; i++) {
            String b = Integer.toBinaryString(i); 
            
            //correct 9 digit format
            int times = 9 - b.length(); 
            for (int j=0; j < times; j++ ){
                 b = "0" + b;
              }

            for (int j = 0; j<9; j++) {
                Secret.getInstance().process(b.charAt(j)); //send digit
                app.updateOutput();
            }
           
            if (app.output.getText().contains("n00bz")) 
                System.out.println(app.output.getText());
             
						//reset
            Secret.getInstance().resetInstance();
            this.app.clearOutput();
        }
    }
