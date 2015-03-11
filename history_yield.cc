TCanvas* c1 = new TCanvas("c1", "c1", 800, 600);
gROOT->Reset("a"); 
TH1F *frame = gPad->DrawFrame(0,0.94,17,1.02);
//TH1F *frame = gPad->DrawFrame(0,2.6,7,3.6);
const int N=17;
const int N1=16;//neutrino-mode
const int N2=7;//horn-off
const int N3=3;
const int No=6;//run44 normalized
const int M=7;
void history_yield()
{
  frame->SetNdivisions(120,"X");
  frame->SetLabelColor(0,"X");
  frame->SetLabelSize(0.06,"Y");
  gStyle->SetEndErrorSize(0);
  c1->SetGrid();

  frame->GetXaxis()->SetTitle("MR Run");
  frame->GetYaxis()->SetTitle("yield ratio");
  frame->GetYaxis()->SetTitleOffset(1.0);
  //run34,36,37,38,42,43,44,45,46,47,48,49,55,56,58
  //horn off 430069 450103 460148 480021
  //horn current corrected
  /*
  double si[N]={33.07,33.00,32.33,32.42,32.72,32.69,32.63,32.52,32.40,32.44,32.38,32.51,32.26,32.19,32.14,31.95};
  double ic[N]={949.0,924.5,905.9,906.2,950.7,953.9,954.6,953.1,951.3,953.8,952.4,953.8,939.2,939.8,933.0,932.7};
  double sim[N3]={20.50,20.58,20.53};//r56,58,59
  double icm[N3]={595.8,598.5,598.4};
  */
  //usual
  
  double si[N1]={32.79,33.00,32.96,32.97,32.47,32.00,32.86,32.72,32.57,32.44,32.28,32.33,32.67,32.53,32.45,32.41};
  double ic[N1]={941.2,922.1,922.7,922.5,943.8,936.5,958.2,958.8,956.1,954.1,949.6,949.0,951.1,949.4,942.1,946.3};
  double sim[N3]={20.67,20.59,20.52};
  double icm[N3]={600.5,598.8,598.2};
  
  double sih[N2]={8.514,8.52,8.474,8.492,8.419,8.407,8.407};//r43,45,46,48,55,56,59
  double ich[N2]={2.609,2.621,2.617,2.617,2.583,2.581,2.589};//r43,45,46,48,55,56,59

  //+250kA
  //double h1[N]={250.59,251.14,253.66,253.57,250.40,249.98,253.13,251.63,251.72,251.21,250.93,250.8,251.8,251.6};
  //double h2[N]={248.59,248.90,252.34,252.31,248.97,247.55,250.46,250.92,250.74,249.99,249.56,249.2,251.9,251.6};
  //double h3[N]={247.62,248.96,251.24,251.17,247.76,246.37,249.22,249.67,249.47,248.75,248.35,248.1,251.0,250.7};
  //double hm1[N3]={};
  //double hm2[N3]={};
  //double hm3[N3]={};
  //double teff[N]={0,0,0,0,99.458,99.752,99.506,99.690,99.520,99.489,99.602,};~r48?
  //double ingrid[N]={1.7137,1.7487,1.7454,1.7415,1.7402,1.7363,1.7391,1.7304,1.7193,1.7186,1.7156,1.718,1.67}; 
  //double ingridE[N]={4.29e-3,2.07e-3,1.75e-3,3.71e-3,1.24e-3,2.68e-3,1.84e-3,1.74e-3,1.22e-3,1.53e-3,2.02e-3,3e-3,0.02};
  //double ingridc[N-1]={0.1532,0.1564,0.1569,0.1546,0.1562,0.1559,0.1568,0.1555,0.1545,0.1549,0.1545,0.1537,0.1496};
  //double ingridcE[N-1]={1.4e-3,6.7e-4,5.6e-4,1.2e-3,4.0e-4,8.6e-4,5.9e-4,5.6e-4,3.9e-4,4.9e-4,6.5e-4,1.0e-3,9.1e-4};
  double tmp[N1]={1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,17},tmp2[N1],tmp3[N1];
  double tmph[N2]={6,8,9,11,13,14,16},tmp2h[N2],tmp3h[N2];
  double tmpm[N3]={14,15,16},tmp2m[N2],tmp3m[N2];
  //double tmpi[N-1];
  double nsi=si[No];
  double nic=ic[No];
  double nsih=sih[0];
  double nich=ich[0];
  double nsim=sim[0];
  double nicm=icm[0];
  //double ningrid=ingrid[No];
  //double ningridc=ingridc[No];
  //double nh1=h1[No];
  //double nh2=h2[No];
  //double nh3=h3[No];
  
  for(int i=0; i<N1; ++i) {
    tmp2[i]=0;
    tmp3[i]=0;
  }
  
  for(int i=0; i<N2; ++i) {
    tmp2h[i]=0;
    tmp3h[i]=0;
  }
  
  //normalization
  for(int i=0; i<N1; ++i) {
    si[i]/=nsi;
    ic[i]/=nic;
    //ingrid[i]/=ningrid;
    //ingridE[i]/=ningrid;
    //h1[i]/=nh1;
    //h2[i]/=nh2;
    //h3[i]/=nh3;
  }
  /*
  for(int i=0; i<N-1; ++i) {
    ingridc[i]/=ningridc;
    ingridcE[i]/=ningridc;
    tmpi[i]=i+1;
  }
  */
  for(int i=0; i<N2; ++i) {
    sih[i]/=nsih;
    ich[i]/=nich;
  }
	
  for(int i=0; i<N3; ++i) {
    sim[i]/=nsim;
    icm[i]/=nicm;
  }

  TString MR[N]={"34","36","37","38","42","43","44","45","46","47","48","49","55","56","58","59","60"};
  TText *t = new TText();
  t->SetTextSize(0.05);
  for(int i=0;i<N;++i) t->DrawText(i+0.7,0.935,MR[i]);

  TGraphErrors *gr[M];
  gr[0]= new TGraphErrors(N1,tmp,si,tmp2,tmp3);
  gr[1]= new TGraphErrors(N1,tmp,ic,tmp2,tmp3);
  gr[2]= new TGraphErrors(N2,tmph,sih,tmp2h,tmp3h);
  gr[3]= new TGraphErrors(N2,tmph,ich,tmp2h,tmp3h);
  //gr[4]= new TGraphErrors(N,tmp,ingrid,tmp2,ingridE);
  //gr[4]= new TGraphErrors(N-1,tmpi,ingridc,tmp2,ingridcE);
  gr[4]= new TGraphErrors(N3,tmpm,sim,tmp2m,tmp3m);
  gr[5]= new TGraphErrors(N3,tmpm,icm,tmp2m,tmp3m);

  /*gr[1]= new TGraphErrors(N,tmp,h1,tmp2,tmp3);
    gr[2]= new TGraphErrors(N,tmp,h2,tmp2,tmp3);
    gr[3]= new TGraphErrors(N,tmp,h3,tmp2,tmp3);*/

  gr[1]->SetMarkerColor(2);
  gr[1]->SetLineColor(2);
  gr[2]->SetMarkerColor(4);
  gr[2]->SetLineColor(4);
  gr[3]->SetMarkerColor(6);
  gr[3]->SetLineColor(6);
  gr[4]->SetMarkerColor(8);
  gr[4]->SetLineColor(8);
  gr[5]->SetMarkerColor(46);
  gr[5]->SetLineColor(46);

  for(int i=0; i<6; ++i){
    gr[i]->SetMarkerStyle(8);
    gr[i]->SetMarkerSize(1.5);
    gr[i]->SetLineWidth(2);
    gr[i]->Draw("same PL");
  }
}
//run29,30,31,32,33
//si   32.55,32.63,32.67,32.72,32.74
//sihc 32.34,32.54,32.86,33.00,32.90
//ic   930.4,933.0,934.5,938.3,939.4
//ichc 924.5,930.6,939.8,946.2,943.8
//run41 good_spill_flag==2
//si 21.65  ic 639.9
//T2KRUN si
//si   32.73 32.95 32.39 32.48
//sihc 32.93 32.61 32.71 32.48

