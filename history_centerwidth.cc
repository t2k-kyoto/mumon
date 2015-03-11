TCanvas* c1 = new TCanvas("c1", "c1", 800, 600);
gROOT->Reset("a"); 
//TH1F *frame = gPad->DrawFrame(0,-3,16,3);//center
//TH1F *frame = gPad->DrawFrame(0,95,16,110);//width x
TH1F *frame = gPad->DrawFrame(0,105,16,130);//width y

//nu-mode
void history_centerwidth()
{

  frame->GetXaxis()->SetTitle("MR Run number");
  //frame->GetYaxis()->SetTitle("horizontal center (cm)");
  //frame->GetYaxis()->SetTitle("vertical center (cm)");
  //frame->GetYaxis()->SetTitle("horizontal width (cm)");
  frame->GetYaxis()->SetTitle("vertical width (cm)");

	const int N=16;
	const int M=2;
	TString MR[N]={"34","36","37","38","42","43","44","45","46","47","48","49","55","56","58","60"};
	//for(int i=0;i<N;++i) frame->GetXaxis()->SetBinLabel(i+1,MR[i]);
	frame->SetNdivisions(120,"X");
	frame->SetLabelColor(0,"X");
	frame->SetLabelSize(0.06,"X");
	frame->SetLabelSize(0.06,"Y");
	frame->GetYaxis()->SetTitleOffset(1.0);
	gStyle->SetEndErrorSize(0);
	c1->SetGrid();
	
	//x center
	//double si[N]={-0.30,0.50,0.13,0.18,-0.52,-0.02,-0.12,-0.55,-0.26,-0.38,0.18,-0.28,0.23,0.06,0.22,0.32};
	//double ic[N]={0.33,1.01,0.99,1.06,0.52,0.92,0.87,0.36,0.85,0.79,0.90,0.84,0.68,0.54,0.57,0.65};
	//y center
	//double si[N]={-2.49,-0.62,-0.62,-0.55,0.25,-0.48,-0.28,-0.78,-1.23,-0.58,-0.48,-0.97,-1.81,-0.15,0.03,-1.03};
	//double ic[N]={1.80,0.82,0.79,0.74,1.22,0.84,2.09,1.06,0.40,0.81,0.91,0.33,0.11,0.74,1.61,0.75};
	//x width
	//double si[N]={103.5,101.4,101.2,102.4,101.7,101.3,102.9,100.7,99.2,98.8,98.0,98.3,102.2,101.7,101.3,102.3};
	//double ic[N]={108.2,106.7,106.1,106.2,106.4,106.4,105.8,105.1,106.0,105.7,105.1,105.5,106.9,106.5,106.3,107.0};
	//y width
	double si[N]={117.2,114.1,113.6,114.7,115.3,113.5,115.7,112.0,111.1,109.6,108.5,108.5,115.7,113.6,113.6,116.1};
        double ic[N]={127.8,124.4,123.5,123.4,123.8,122.9,124.7,122.1,124.5,123.6,122.7,122.9,125.5,123.8,124.1,125.5};

	double tmp[N];
	for(int i=0;i<N;++i) tmp[i]=i+1;
	/*TH1F *h = new TH1F("h","",N,tmp[0],tmp[N-1]);
	for(int i=0;i<N;++i) h->GetXaxis()->SetBinLabel(i+1,MR[i]);
	h->GetXaxis()->SetLabelSize(0.06);
	h->SetLineColor(0);
	h->Draw("same");*/
	TText *t = new TText();
	t->SetTextSize(0.05);
	//for(int i=0;i<N;++i) t->DrawText(tmp[i]-0.3,-3.4,MR[i]);//center
	//for(int i=0;i<N;++i) t->DrawText(tmp[i]-0.3,94.0,MR[i]);//x width
	for(int i=0;i<N;++i) t->DrawText(tmp[i]-0.3,103.25,MR[i]);//y width

	TGraph *gr[2];
	gr[0]= new TGraph(N,tmp,si);
	gr[1]= new TGraph(N,tmp,ic);

	for(int i=0; i<M; i++){
	  gr[i]->SetMarkerColor(i+1);
	  gr[i]->SetLineColor(i+1);
	  gr[i]->SetMarkerStyle(8);
	  gr[i]->SetMarkerSize(1.5);
	  gr[i]->SetLineWidth(2);
	  gr[i]->Draw("same PL");
	}
}

