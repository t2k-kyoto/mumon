import sys,os,glob,datetime
from ROOT import *
from array import array
gROOT.LoadMacro("T2KStyle.C")
gROOT.LoadMacro("T2KLabels.C")
SetT2KStyle()
##

#Default TChain from data
def DataTChain(filelist,tree_name):
  tchain = TChain()
  for bsd_file in filelist:
    tchain.Add(bsd_file+'/'+tree_name)
  return tchain


#New TChain with event selections included
def NewTChain(old_tchain):
  new_tchain = old_tchain.CloneTree(0)
  n_entries = old_tchain.GetEntries()
  for i in xrange(n_entries):
    old_tchain.GetEvent(i)
    if old_tchain.mumon[3] > -1:
      #print old_tchain.mumon[3]
      #print type(old_tchain.midas_event)
      new_tchain.Fill()
  #print new_tchain.GetEntries()
  return new_tchain


#Plots
def MakeHists(tchain,branch_name,hist_name):
  tchain.Draw(branch_name)
  htemp = TH1F(gPad.GetPrimitive("htemp"))
  htemp.SetName(hist_name)
  return htemp

def MakePlots(mode,tchain,start_time,end_time):
  #Convert time
  start = float(start_time.Convert()) #+9h for JST
  end = float(end_time.Convert())
  #print 'start,end',start,end
  #Get number of entries
  n_entries = tchain.GetEntries()
  #Create histograms
  if mode == 'nu':
    #Centres
    hist_si_x_centre = TH2F('hist_si_x_centre','si_x_centre;Date-time;Si x position (cm)',400,start,end,300,-3.,3.)
    hist_si_y_centre = TH2F('hist_si_y_centre','si_y_centre;Date-time;Si y position (cm)',400,start,end,300,-3.,3.)
    hist_ic_x_centre = TH2F('hist_ic_x_centre','ic_x_centre;Date-time;IC x position (cm)',400,start,end,300,-3.,3.)
    hist_ic_y_centre = TH2F('hist_ic_y_centre','ic_y_centre;Date-time;IC y position (cm)',400,start,end,300,-3.,3.)
    #Width
    hist_si_x_width = TH2F('hist_si_x_width','si_x_width;Date-time;Si x width (cm)',400,start,end,400,100,105)
    hist_si_y_width = TH2F('hist_si_y_width','si_y_width;Date-time;Si y width (cm)',400,start,end,400,111,120)
    hist_ic_x_width = TH2F('hist_ic_x_width','ic_x_width;Date-time;IC x width (cm)',400,start,end,400,105,109)
    hist_ic_y_width = TH2F('hist_ic_y_width','ic_y_width;Date-time;IC y width (cm)',400,start,end,400,121,130)
    #Horn currents
    #nu mode ranges
    hist_hc1 = TH2F('hist_hc1','hc1;Date-time;Horn 1 Current (kA)',400,start,end,300,248.,252.)
    hist_hc2 = TH2F('hist_hc2','hc2;Date-time;Horn 2 Current (kA)',400,start,end,300,248.,252.)
    hist_hc3 = TH2F('hist_hc3','hc3;Date-time;Horn 3 Current (kA)',400,start,end,300,248.,252.)
    #Yeilds
    #nu mode ranges
    hist_sich_ct5np = TH2F('hist_sich_ct5np','sich_ct5np;Date-time;Si charge/POT charge',400,start,end,300,198,205)
    hist_icch_ct5np = TH2F('hist_icch_ct5np','icch_ct5np;Date-time;IC charge/POT charge',400,start,end,300,5.8,6.)
    #Horn current Vs yield
    #nu mode ranges
    hist_si_hc1 = TH2F('hist_si_hc1','si_hc1;Horn 1 current (kA);Si charge/POT charge',200,245.,255.,200,198,205)
    hist_si_hc2 = TH2F('hist_si_hc2','si_hc2;Horn 2 current (kA);Si charge/POT charge',200,245.,255.,200,198,205)
    hist_si_hc3 = TH2F('hist_si_hc3','si_hc3;Horn 3 current (kA);Si charge/POT charge',200,245.,255.,200,198,205)
    hist_ic_hc1 = TH2F('hist_ic_hc1','ic_hc1;Horn 1 current (kA);IC charge/POT charge',200,245.,255.,200,5.8,6.)
    hist_ic_hc2 = TH2F('hist_ic_hc2','ic_hc2;Horn 2 current (kA);IC charge/POT charge',200,245.,255.,200,5.8,6.)
    hist_ic_hc3 = TH2F('hist_ic_hc3','ic_hc3;Horn 3 current (kA);IC charge/POT charge',200,245.,255.,200,5.8,6.)
    #Yields with horn current correction applied
    hist_sich_ct5np_hcc = TH2F('hist_sich_ct5np_hcc','sich_ct5np_hcc;Date-time;Si charge/POT charge [corrected]',400,start,end,300,198,205)
    hist_icch_ct5np_hcc = TH2F('hist_icch_ct5np_hcc','icch_ct5np_hcc;Date-time;IC charge/POT charge [corrected]',400,start,end,300,5.8,6.)
  
  if mode == 'antinu':
    hist_si_x_centre = TH2F('hist_si_x_centre','si_x_centre;Date-time;Si x position (cm)',400,start,end,300,-3.,3.)
    hist_si_y_centre = TH2F('hist_si_y_centre','si_y_centre;Date-time;Si y position (cm)',400,start,end,300,-3.,3.)
    hist_ic_x_centre = TH2F('hist_ic_x_centre','ic_x_centre;Date-time;IC x position (cm)',400,start,end,300,-3.,3.)
    hist_ic_y_centre = TH2F('hist_ic_y_centre','ic_y_centre;Date-time;IC y position (cm)',400,start,end,300,-3.,3.)
    #Width
    hist_si_x_width = TH2F('hist_si_x_width','si_x_width;Date-time;Si x width (cm)',400,start,end,400,96,100)
    hist_si_y_width = TH2F('hist_si_y_width','si_y_width;Date-time;Si y width (cm)',400,start,end,400,102,106)
    hist_ic_x_width = TH2F('hist_ic_x_width','ic_x_width;Date-time;IC x width (cm)',400,start,end,400,101,106)
    hist_ic_y_width = TH2F('hist_ic_y_width','ic_y_width;Date-time;IC y width (cm)',400,start,end,400,111,116)
    #Horn currents
    #anti-nu mode ranges
    hist_hc1 = TH2F('hist_hc1','hc1;Date-time;Horn 1 Current (kA)',400,start,end,300,-252.,-249.5)
    hist_hc2 = TH2F('hist_hc2','hc2;Date-time;Horn 2 Current (kA)',400,start,end,300,-251.5,-248.5)
    hist_hc3 = TH2F('hist_hc3','hc3;Date-time;Horn 3 Current (kA)',400,start,end,300,-250.3,-248.)
    #Yeilds
    #anti-nu mode ranges
    hist_sich_ct5np = TH2F('hist_sich_ct5np','sich_ct5np;Date-time;Si charge/POT charge',400,start,end,300,125,132)
    hist_icch_ct5np = TH2F('hist_icch_ct5np','icch_ct5np;Date-time;IC charge/POT charge',400,start,end,300,3.65,3.85)
    #Horn current Vs yield
    #nu mode ranges
    hist_si_hc1 = TH2F('hist_si_hc1','si_hc1;Horn 1 current (kA);Si charge/POT charge',200,-252.,-248.,200,125,132)
    hist_si_hc2 = TH2F('hist_si_hc2','si_hc2;Horn 2 current (kA);Si charge/POT charge',200,-252.,-248.,200,125,132)
    hist_si_hc3 = TH2F('hist_si_hc3','si_hc3;Horn 3 current (kA);Si charge/POT charge',200,-252.,-248.,200,125,132)
    hist_ic_hc1 = TH2F('hist_ic_hc1','ic_hc1;Horn 1 current (kA);IC charge/POT charge',200,-252.,-248.,200,3.65,3.85)
    hist_ic_hc2 = TH2F('hist_ic_hc2','ic_hc2;Horn 2 current (kA);IC charge/POT charge',200,-252.,-248.,200,3.65,3.85)
    hist_ic_hc3 = TH2F('hist_ic_hc3','ic_hc3;Horn 3 current (kA);IC charge/POT charge',200,-252.,-248.,200,3.65,3.85)
    #Yields with horn current correction applied
    hist_sich_ct5np_hcc = TH2F('hist_sich_ct5np_hcc','sich_ct5np_hcc;Date-time;Si charge/POT charge [corrected]',400,start,end,300,125,132)
    hist_icch_ct5np_hcc = TH2F('hist_icch_ct5np_hcc','icch_ct5np_hcc;Date-time;IC charge/POT charge [corrected]',400,start,end,300,3.65,3.85)

  if mode == 'off':
    hist_si_x_centre = TH2F('hist_si_x_centre','si_x_centre;Date-time;Si x position (cm)',400,start,end,300,-5.,5.)
    hist_si_y_centre = TH2F('hist_si_y_centre','si_y_centre;Date-time;Si y position (cm)',400,start,end,300,-5.,5.)
    hist_ic_x_centre = TH2F('hist_ic_x_centre','ic_x_centre;Date-time;IC x position (cm)',400,start,end,300,-5.,5.)
    hist_ic_y_centre = TH2F('hist_ic_y_centre','ic_y_centre;Date-time;IC y position (cm)',400,start,end,300,-5.,5.)
    #Width
    hist_si_x_width = TH2F('hist_si_x_width','si_x_width;Date-time;Si x width (cm)',400,start,end,400,130,140)
    hist_si_y_width = TH2F('hist_si_y_width','si_y_width;Date-time;Si y width (cm)',400,start,end,400,145,155)
    hist_ic_x_width = TH2F('hist_ic_x_width','ic_x_width;Date-time;IC x width (cm)',400,start,end,400,145,155)
    hist_ic_y_width = TH2F('hist_ic_y_width','ic_y_width;Date-time;IC y width (cm)',400,start,end,400,110,125)
    #Horn currents
    #anti-nu mode ranges
    hist_hc1 = TH2F('hist_hc1','hc1;Date-time;Horn 1 Current (kA)',400,start,end,300,-0.001,0.001)
    hist_hc2 = TH2F('hist_hc2','hc2;Date-time;Horn 2 Current (kA)',400,start,end,300,-0.001,0.001)
    hist_hc3 = TH2F('hist_hc3','hc3;Date-time;Horn 3 Current (kA)',400,start,end,300,-0.001,0.001)
    #Yeilds
    #anti-nu mode ranges
    hist_sich_ct5np = TH2F('hist_sich_ct5np','sich_ct5np;Date-time;Si charge/POT charge',400,start,end,300,49,52)
    hist_icch_ct5np = TH2F('hist_icch_ct5np','icch_ct5np;Date-time;IC charge/POT charge',400,start,end,300,1.45,1.55)
    #Horn current Vs yield
    #horn current off ranges
    hist_si_hc1 = TH2F('hist_si_hc1','si_hc1;Horn 1 current (kA);Si charge/POT charge',200,-0.001,0.001,200,199,203)
    hist_si_hc2 = TH2F('hist_si_hc2','si_hc2;Horn 2 current (kA);Si charge/POT charge',200,-0.001,0.001,200,199,203)
    hist_si_hc3 = TH2F('hist_si_hc3','si_hc3;Horn 3 current (kA);Si charge/POT charge',200,-0.001,0.001,200,199,203)
    hist_ic_hc1 = TH2F('hist_ic_hc1','ic_hc1;Horn 1 current (kA);IC charge/POT charge',200,-0.001,0.001,200,5.6,6.1)
    hist_ic_hc2 = TH2F('hist_ic_hc2','ic_hc2;Horn 2 current (kA);IC charge/POT charge',200,-0.001,0.001,200,5.6,6.1)
    hist_ic_hc3 = TH2F('hist_ic_hc3','ic_hc3;Horn 3 current (kA);IC charge/POT charge',200,-0.001,0.001,200,5.6,6.1)
    #Yields with horn current correction applied
    hist_sich_ct5np_hcc = TH2F('hist_sich_ct5np_hcc','sich_ct5np_hcc;Date-time;Si charge/POT charge [corrected]',400,start,end,300,49,52)
    hist_icch_ct5np_hcc = TH2F('hist_icch_ct5np_hcc','icch_ct5np_hcc;Date-time;IC charge/POT charge [corrected]',400,start,end,300,1.8,1.9)

  #avg yield for history
  r60y = 0.
  r60p = 0.
  r59y = 0.
  r59p = 0.
  #Loop over entries
  for i in xrange(n_entries):
    tchain.GetEvent(i)
#anti-nu runs in MR Run58
    if tchain.spillnum < 1830240:
# Cuts already included in qsd files
#    if tchain.run_type == 1:
#      if thain.trigger_flag == 2:
#        if tchain.good_gps_flag == 1:
#          if tchain.ct_np[36] > 1e11:
      #Better variable names
      time = float(tchain.trg_sec[0])
      #print time
      si_x_centre = tchain.mumon[2]
      si_y_centre = tchain.mumon[4]
      ic_x_centre = tchain.mumon[8]
      ic_y_centre = tchain.mumon[10]
      si_x_width = tchain.mumon[3]
      si_y_width = tchain.mumon[5]
      ic_x_width = tchain.mumon[9]
      ic_y_width = tchain.mumon[11]
      #print 'hist_si_x_centre,si_y_centre,ic_x_centre,ic_y_centre', si_x_centre,si_y_centre,ic_x_centre,ic_y_centre
      #print 'si_x_width,si_y_width,ic_x_width,ic_y_width', si_x_width,si_y_width,ic_x_width,ic_y_width
      sich = float(tchain.mumon[0]) #nC
      icch = float(tchain.mumon[6]) #nC
      #print sich,icch
      ct5np = float(tchain.ct_np[36]) #ct_np[36] --> CT5 protons per spill
      sich_ct5np = sich/ct5np
      icch_ct5np = icch/ct5np
      #print sich_ct5np,icch_ct5np
      #Applying horn current correction
      hc1 = tchain.hct[0] #HC1 kA
      hc2 = tchain.hct[5] #HC2 kA
      hc3 = tchain.hct[10] #HC3 kA
      #print 'hc1,hc2,hc3',hc1+hc2+hc3
      if 700. < (hc1+hc2+hc3) < 800.:
        #print 'poo',(1+(hc1+hc2+hc3-750.)*2.667e-3)
        sich_ct5np_hcc = sich_ct5np*(1+(hc1+hc2+hc3-750.)*2.667e-3)
        icch_ct5np_hcc = icch_ct5np*(1+(hc1+hc2+hc3-750.)*2.667e-3)
      elif -800. < (hc1+hc2+hc3) < -700.:
        sich_ct5np_hcc = sich_ct5np*(1+(hc1+hc2+hc3+750.)*2.367e-3)
        icch_ct5np_hcc = icch_ct5np*(1+(hc1+hc2+hc3+750.)*2.367e-3)
      else:
        sich_ct5np_hcc = sich_ct5np
        icch_ct5np_hcc = icch_ct5np
      #Convert to different units, #nC->C, protons per spill Nprotons->C
      sich_ct5np = sich_ct5np*(1e-9)/(1.602e-19)
      sich_ct5np_hcc = sich_ct5np_hcc*(1e-9)/(1.602e-19)
      icch_ct5np = icch_ct5np*(1e-9)/(1.602e-19)
      icch_ct5np_hcc = icch_ct5np_hcc*(1e-9)/(1.602e-19)
      #if tchain.mrrun == 60: 
      #print 'reg and corr sich_ct5np',sich_ct5np,sich_ct5np_hcc
      #print 'reg and corr icch_ct5np',icch_ct5np,icch_ct5np_hcc
      #Fill histograms
      hist_hc1.Fill(time,hc1)
      hist_hc2.Fill(time,hc2)
      hist_hc3.Fill(time,hc3)
      hist_si_x_centre.Fill(time,si_x_centre)
      hist_si_y_centre.Fill(time,si_y_centre)
      hist_ic_x_centre.Fill(time,ic_x_centre)
      hist_ic_y_centre.Fill(time,ic_y_centre)
      hist_si_x_width.Fill(time,si_x_width)
      hist_si_y_width.Fill(time,si_y_width)
      hist_ic_x_width.Fill(time,ic_x_width)
      hist_ic_y_width.Fill(time,ic_y_width)
      hist_sich_ct5np.Fill(time,sich_ct5np)
      hist_icch_ct5np.Fill(time,icch_ct5np)
      hist_sich_ct5np_hcc.Fill(time,sich_ct5np_hcc)
      hist_icch_ct5np_hcc.Fill(time,icch_ct5np_hcc)
      hist_si_hc1.Fill(hc1,sich_ct5np)
      hist_si_hc2.Fill(hc2,sich_ct5np)
      hist_si_hc3.Fill(hc3,sich_ct5np)
      hist_ic_hc1.Fill(hc1,icch_ct5np)
      hist_ic_hc2.Fill(hc2,icch_ct5np)
      hist_ic_hc3.Fill(hc3,icch_ct5np)
  #Make list of histograms to be plotted
  hist_list = [\
      hist_si_x_centre,hist_si_y_centre,\
      hist_ic_x_centre,hist_ic_y_centre,\
      hist_si_x_width,hist_si_y_width,\
      hist_ic_x_width,hist_ic_y_width,\
      hist_hc1,hist_hc2,hist_hc3,\
      hist_sich_ct5np,hist_icch_ct5np,\
      hist_si_hc1,hist_si_hc2,hist_si_hc3,hist_ic_hc1,hist_ic_hc2,hist_ic_hc3,\
      hist_sich_ct5np_hcc,hist_icch_ct5np_hcc\
      ]
  #Return list of histograms
  return hist_list

def DrawPlots(hist_list,start,end):
  l = TLatex()
  for hist in hist_list:
    name = hist.GetName()
    #Format the histogram
    if hist.GetXaxis().GetTitle() == 'Date-time':
      hist.GetXaxis().SetTitle('Date')
      hist.GetXaxis().SetTimeDisplay(1)
      #hist.GetXaxis().SetTimeOffset(start.Convert())
      hist.GetXaxis().SetTimeFormat('%d%b')
      hist.SetNdivisions(4,"X")
    hist.SetLabelSize(0.05,"X")
    hist.SetLabelSize(0.05,"Y")
    hist.SetTitleSize(0.06,"X")
    hist.SetTitleSize(0.06,"Y")
    hist.SetTitleOffset(1,"X")
    hist.SetTitleOffset(1.1,"Y")
    hist.Draw('colz')
#    if 'sich_ct5np_hcc' in name:
      #legend = TLegend()
      #legend.SetHeader('Horn Current Correction Applied')
      #legend.Draw('same')
    #Edit the pad and save
    gPad.SetMargin(0.15,0.16,0.14,0.1)
    gPad.Print('corr_'+name+'.pdf')
  return None
###
###MAIN
if __name__ == "__main__":
  #Choose mode: 'nu','antinu','off'
  mode = 'antinu'
  #Choose the input data to be used 
  #e.g. run060 means all MR run 60 data
  #nu run 550089 & spillnum < 179990 for neutrino mode correction
  #and run 550116 & spillnum < 1830240 for anti-neutrino mode correction
  #run 550111 is horn off data
  bsd_dir = "/home/beam_summary/beam_summary/qsd/p06/t2krun5/"
  bsd_files = glob.glob(bsd_dir+"bsd_run0550116*root")
  bsd_tree_name = 'bsd'
  bsd_dir = "/home/beam_summary/beam_summary/bsd/v01/t2krun6/"
  bsd_files = glob.glob(bsd_dir+"bsd_run058*.root") + glob.glob(bsd_dir+"bsd_run059*.root")
  bsd_tree_name = 'bsd'
  
  #Choose the time and date range in JST (yyyy,mm,dd,hh,mm,ss)
  start_time = TDatime(2014,11,04,10,00,00)
  end_time = TDatime(2014,12,22,20,00,00)

  #Choose the output rootfile name
  output_filename = 'corr_t2k_collab_meeting.root'

  #Get original data TChain
  bsd_tree = DataTChain(bsd_files,bsd_tree_name)
  
  #Create rootfile to save the histograms
  output_hists_file = TFile(output_filename,'recreate')

  #Make new TChain from the list of rootfiles
  new_tree = NewTChain(bsd_tree)
  new_tree.Write()
  
  #Make and save hists of the tree variables used
  #for key in ttree_dict.keys():
  #  MakeHists(new_tree,ttree_dict[key],key).Write()
  
  #Make and save histograms for the meeting
  plots = MakePlots(mode,new_tree,start_time,end_time)
  for plot in plots:
    plot.Write()
  DrawPlots(plots,start_time,end_time)

  #Save and close the rootfile
  output_hists_file.Close()
###
###
