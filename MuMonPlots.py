import sys,os,glob,datetime
from ROOT import *
from array import array
gROOT.LoadMacro("AtlasStyle.C")
gROOT.LoadMacro("AtlasLabels.C")
SetAtlasStyle()


#Default TChain from data
def DataTChain(filelist,tree_name):
  tchain = TChain()
  for qsd_file in qsd_files:
    tchain.Add(qsd_file+'/'+tree_name)
  return tchain


#Dictionary for TTree variables
def TTreeDict():
  tree_dict = { \
      'si_tot_charge':'mumon[0]',\
      'si_x_centre':'mumon[2]',\
      'si_y_centre':'mumon[4]',\
      'ic_tot_charge':'mumon[6]',\
      'ic_x_centre':'mumon[8]',\
      'ic_y_centre':'mumon[10]',\
      }
  return tree_dict


#New TChain with event selections included
def NewTChain(old_tchain,tree_dict):
  new_tchain = old_tchain.CloneTree(0)
  n_entries = old_tchain.GetEntries()
  for i in xrange(n_entries):
    old_tchain.GetEvent(i)
    if old_tchain.mumon[3] > -1:
      #print old_tchain.mumon[3]
      #print type(old_tchain.midas_event)
      new_tchain.Fill()
  print new_tchain.GetEntries()
  return new_tchain


#Plots
def MakeHists(tchain,branch_name,hist_name):
  tchain.Draw(branch_name)
  htemp = TH1F(gPad.GetPrimitive("htemp"))
  htemp.SetName(hist_name)
  return htemp

def MakePlots(tchain,tree_dict,start_time,end_time):
  #Convert time
  start = float(start_time.Convert()+32400) #+9h for JST
  end = float(end_time.Convert()+32400)
  #Get number of entries
  n_entries = tchain.GetEntries()
  #Create histograms
  hist_si_x_centre = TH2F('hist_si_x_centre','si_x_centre;Date-time;Si x position (cm)',200,start,end,200,-5.5,5.5)
  hist_si_y_centre = TH2F('hist_si_y_centre','si_y_centre;Date-time;Si y position (cm)',200,start,end,200,-5.5,5.5)
  hist_sich_ct5np = TH2F('hist_sich_ct5np','sich_ct5np;Date-time;Si total charge/Number of protons (nC)',400,start,end,400,1.9e-8,2.2e-8)
  hist_ic_x_centre = TH2F('hist_ic_x_centre','ic_x_centre;Date-time;IC x position (cm)',200,start,end,200,-5.5,5.5)
  hist_ic_y_centre = TH2F('hist_ic_y_centre','ic_y_centre;Date-time;IC y position (cm)',200,start,end,200,-5.5,5.5)
  hist_icch_ct5np = TH2F('hist_icch_ct5np','icch_ct5np;Date-time;IC total charge/Number of protons (nC)',400,start,end,400,5.8e-10,6.2e-10)
  #Loop over entries
  for i in xrange(n_entries):
    tchain.GetEvent(i)
    #Better variable names
    time = tchain.trg_sec[0]
    si_x_centre = tchain.mumon[2]
    si_y_centre = tchain.mumon[4]
    ic_x_centre = tchain.mumon[8]
    ic_y_centre = tchain.mumon[10]
    sich = float(tchain.mumon[0])
    icch = float(tchain.mumon[6])
    ct5np = float(tchain.ct_np[36]) #ct_np[36] --> CT5 protons per spill
    sich_ct5np = sich/ct5np
    #print 'charge,np',sich,ct5np
    icch_ct5np = icch/ct5np
    #print sich,ct5np,sich_ct5np
    #Fill histograms
    hist_si_x_centre.Fill(time,si_x_centre)
    hist_si_y_centre.Fill(time,si_y_centre)
    hist_sich_ct5np.Fill(time,sich_ct5np)
    hist_ic_x_centre.Fill(time,ic_x_centre)
    hist_ic_y_centre.Fill(time,ic_y_centre)
    hist_icch_ct5np.Fill(time,icch_ct5np)
    #print sich_ct5np,icch_ct5np
  #Make list of histograms to be plotted
  hist_list = [\
      hist_si_x_centre,\
      hist_si_y_centre,\
      hist_sich_ct5np,\
      hist_ic_x_centre,\
      hist_ic_y_centre,\
      hist_icch_ct5np\
      ]
  #for hist in hist_list:
    #hist.GetXaxis().SetTimeDisplay(1)
    #hist.GetXaxis().SetTimeFormat('%m/%d%F')#('%y-%m-%d%F')
  #Return list of histograms
  return hist_list

def DrawPlots(hist_list):
  l = TLatex()
  for hist in hist_list:
    name = hist.GetName()
    #Format the histogram
    hist.GetXaxis().SetTimeDisplay(1)
    hist.GetXaxis().SetTimeFormat('%m/%d-%Hh')
    hist.SetNdivisions(6,"X")
    hist.SetLabelSize(0.04,"X")
    hist.SetLabelSize(0.04,"Y")
    hist.SetTitleSize(0.04,"X")
    hist.SetTitleSize(0.04,"Y")
    hist.SetTitleOffset(0.9,"X")
    hist.SetTitleOffset(0.7,"Y")
    hist.Draw('colz')
    #Edit the pad and save
    gPad.SetMargin(0.15,0.16,0.14,0.1)
    gPad.Print(name+'.pdf')
  return None
###
###MAIN
if __name__ == "__main__":
  
  #Choose the input data to be used 
  #e.g. run060 means all MR run 60 data
  qsd_dir = "/home/beam_summary/beam_summary/qsd/p06/t2krun6/"
  qsd_files = glob.glob(qsd_dir+"bsd_run060*.root")
  qsd_tree_name = 'bsd'
  #bsd_dir = "/home/beam_summary/beam_summary/bsd/v01/t2krun6/"
  #bsd_files = glob.glob(bsd_dir+"bsd_run0590153_00v01.root")
  
  #Choose the time and date range in JST (yyyy,mm,dd,hh,mm,ss)
  start_time = TDatime(2015,01,12,07,00,00)
  end_time = TDatime(2015,01,16,10,00,00)

  #Choose the output rootfile name
  output_filename = 'test_plots_20150122.root'

  #Dictionary for TTree branches
  ttree_dict = TTreeDict()

  #Get original data TChain
  qsd_tree = DataTChain(qsd_files,qsd_tree_name)
  
  #Create rootfile to save the histograms
  output_hists_file = TFile(output_filename,'recreate')

  #Make new TChain from the list of rootfiles
  new_tree = NewTChain(qsd_tree,ttree_dict)
  new_tree.Write()
  
  #Make and save hists of the tree variables used
  #for key in ttree_dict.keys():
  #  MakeHists(new_tree,ttree_dict[key],key).Write()
  
  #Make and save histograms for the meeting
  plots = MakePlots(new_tree,ttree_dict,start_time,end_time)
  for plot in plots:
    plot.Write()
  DrawPlots(plots)

  #Save and close the rootfile
  output_hists_file.Close()
###
###
